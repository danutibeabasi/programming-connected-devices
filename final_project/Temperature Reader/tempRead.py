import random
import struct
import time
from time import sleep_ms

import bluetooth
import micropython
import ubluetooth
from micropython import const

from ble_advertising import decode_name, decode_services

"""
Requirements
Esp32 (central role) is supposed to connect to nrf52 avertisement
"""
SCAN_DURATION = 60000  # 1 minute scan

_IRQ_CENTRAL_CONNECT = const(1)
_IRQ_CENTRAL_DISCONNECT = const(2)
_IRQ_GATTS_WRITE = const(3)
_IRQ_GATTS_READ_REQUEST = const(4)
_IRQ_SCAN_RESULT = const(5)
_IRQ_SCAN_DONE = const(6)
_IRQ_PERIPHERAL_CONNECT = const(7)
_IRQ_PERIPHERAL_DISCONNECT = const(8)
_IRQ_GATTC_SERVICE_RESULT = const(9)
_IRQ_GATTC_SERVICE_DONE = const(10)
_IRQ_GATTC_CHARACTERISTIC_RESULT = const(11)
_IRQ_GATTC_CHARACTERISTIC_DONE = const(12)
_IRQ_GATTC_DESCRIPTOR_RESULT = const(13)
_IRQ_GATTC_DESCRIPTOR_DONE = const(14)
_IRQ_GATTC_READ_RESULT = const(15)
_IRQ_GATTC_READ_DONE = const(16)
_IRQ_GATTC_WRITE_DONE = const(17)
_IRQ_GATTC_NOTIFY = const(18)
_IRQ_GATTC_INDICATE = const(19)

_ADV_IND = const(0x00)
_ADV_DIRECT_IND = const(0x01)
_ADV_SCAN_IND = const(0x02)
_ADV_NONCONN_IND = const(0x03)

_UART_SERVICE_UUID = bluetooth.UUID("6E400001-B5A3-F393-E0A9-E50E24DCCA9E")
_UART_RX_CHAR_UUID = bluetooth.UUID("6E400002-B5A3-F393-E0A9-E50E24DCCA9E")
_UART_TX_CHAR_UUID = bluetooth.UUID("6E400003-B5A3-F393-E0A9-E50E24DCCA9E")

# Add your own nrf creds here after scanning
DEVICE_ADDR_TYPE = 1
DEVICE_ADDR = b'\xc66fO[\x06'


class BLE:
    def __init__(self, name):
        self.name = name
        self.ble = ubluetooth.BLE()
        self.ble.active(True)
        self._reset()
        self.ble.irq(self.ble_irq)
        # You can comment out the line below once youve scanned and gotten your
        # nrf device addr_type and addr to be passed in the connect function
        self.scanner()
        # Connect to nrf52
        self.connect_nrf(addr_type=DEVICE_ADDR_TYPE, addr=DEVICE_ADDR)
        # Read data over uart for test
        while self.is_connected():
            self.read(callback=print)
            sleep_ms(2000)

    def _reset(self):
        self._name = None
        self._addr_type = None
        self._addr = None

        # Callbacks for completion of various operations.
        # These reset back to None after being invoked.
        self._scan_callback = None
        self._conn_callback = None
        self._read_callback = None

        # Value from nrf52
        self._value = None

        # Persistent callback for when new data is notified from the device.
        self._notify_callback = None

        # Connected device.
        self._conn_handle = None
        self._start_handle = None
        self._end_handle = None
        self._tx_handle = None
        self._rx_handle = None
        self._value_handle = None

    # Returns true if we've successfully connected and discovered characteristics.
    def is_connected(self):
        return (
            self._conn_handle is not None
            and self._tx_handle is not None
            and self._rx_handle is not None
        )

    def ble_irq(self, event, data):
        if event == _IRQ_SCAN_RESULT:
            """Scan result"""
            addr_type, addr, adv_type, rssi, adv_data = data
            """
            addr_type values indicate public or random addresses:
                0x00 - PUBLIC
                0x01 - RANDOM (either static, RPA, or NRPA, the type is encoded in the address itself)

            adv_type values correspond to the Bluetooth Specification:
                0x00 - ADV_IND - connectable and scannable undirected advertising
                0x01 - ADV_DIRECT_IND - connectable directed advertising
                0x02 - ADV_SCAN_IND - scannable undirected advertising
                0x03 - ADV_NONCONN_IND - non-connectable undirected advertising
                0x04 - SCAN_RSP - scan response
            """
            print(
                f"Found peripheral addr_type: {addr_type},addr: {bytes(addr)},adv_type: {adv_type},rssi: {rssi},adv_data: {decode_name(adv_data) or '?'}"
            )
        elif event == _IRQ_SCAN_DONE:
            # Scan done/ended
            print("scan ended")

        elif event == _IRQ_PERIPHERAL_CONNECT:
            print("CConnected successfully!")
            conn_handle, addr_type, addr = data
            if addr_type == self._addr_type and addr == self._addr:
                self._conn_handle = conn_handle
                self.ble.gattc_discover_services(self._conn_handle)
        elif event == _IRQ_PERIPHERAL_DISCONNECT:
            # Disconnect (either initiated by us or the remote end).
            conn_handle, _, _ = data
            if conn_handle == self._conn_handle:
                # If it was initiated by us, it'll already be reset.
                self._reset()
        elif event == _IRQ_GATTC_SERVICE_RESULT:
            # Connected device returned a service.
            conn_handle, start_handle, end_handle, uuid = data
            print("service", data)
            if conn_handle == self._conn_handle and uuid == _UART_SERVICE_UUID:
                self._start_handle, self._end_handle = start_handle, end_handle

        elif event == _IRQ_GATTC_SERVICE_DONE:
            # Service query complete.
            if self._start_handle and self._end_handle:
                self.ble.gattc_discover_characteristics(
                    self._conn_handle, self._start_handle, self._end_handle
                )
            else:
                print("Failed to find uart service.")

        elif event == _IRQ_GATTC_CHARACTERISTIC_RESULT:
            # Connected device returned a characteristic.
            conn_handle, def_handle, value_handle, properties, uuid = data
            if conn_handle == self._conn_handle and uuid == _UART_RX_CHAR_UUID:
                self._rx_handle = value_handle
            if conn_handle == self._conn_handle and uuid == _UART_TX_CHAR_UUID:
                self._tx_handle = value_handle

        elif event == _IRQ_GATTC_CHARACTERISTIC_DONE:
            # Characteristic query complete.
            if self._tx_handle is not None and self._rx_handle is not None:
                # We've finished connecting and discovering device, fire the connect callback.
                if self._conn_callback:
                    self._conn_callback()
            else:
                print("Failed to find uart rx characteristic.")
        elif event == _IRQ_GATTC_READ_RESULT:
            # A read completed successfully.
            self._value = data
            if self._read_callback:
                self._read_callback(self._value)
                # Pass the data to the display_oled function as a string
                self.display_oled(str(self._value))
                self._read_callback = None
            # A read completed successfully.
            conn_handle, value_handle, char_data = data
            print(f"Received {char_data} from nrf52")
            if conn_handle == self._conn_handle and value_handle == self._value_handle:
                if self._read_callback:
                    self._read_callback(self._value)
                    self._read_callback = None
#            conn_handle, value_handle, char_data = data
#            print(f"Received {char_data} from nrf52")
#             if conn_handle == self._conn_handle and value_handle == self._value_handle:
#                if self._read_callback:
#                    self._read_callback(self._value)
#                    self._read_callback = None

        elif event == _IRQ_GATTC_WRITE_DONE:
            conn_handle, value_handle, status = data
            print("TX complete")

        elif event == _IRQ_GATTC_NOTIFY:
            conn_handle, value_handle, notify_data = data
            if conn_handle == self._conn_handle and value_handle == self._tx_handle:
                if self._notify_callback:
                    self._notify_callback(notify_data)

    # Send data over the UART
    def write(self, v, response=False):
        if not self.is_connected():
            return
        self.ble.gattc_write(
            self._conn_handle, self._rx_handle, v, 1 if response else 0
        )

    # Read data sent over the UART
    def read(self, callback):
        if not self.is_connected():
            return
        print("Reading Data from NRF52")
        self._read_callback = callback
        self.ble.gattc_read(self._conn_handle, self._value_handle)
    
    # Display the data on OLED
    def display_oled(self, data):
        # Create DHT22 object
        d = dht.DHT22(Pin(27))

        # Create I2C Interface
        i2c = SoftI2C(sda=Pin(23), scl=Pin(22))
        display = ssd1306.SSD1306_I2C(128, 64, i2c)
        display.poweron()

        currentTemperature = ''
        currentHumidity = ''

        #display time, temperature and humidity every sec
        while True:
            for t in time.gmtime():
                currenttime = currenttime + str(t)
            print(currenttime)
            display.text(currenttime, 0, 2, 1)
            display.text(str(data), 0, 12, 1)
            #display.text(humidityStr, 0, 22, 1)
            display.show()
            time.sleep(1)

    def advertiser(self):
        name = bytes(self.name, "UTF-8")
        self.ble.gap_advertise(
            100, bytearray("\x02\x01\x02") + bytearray((len(name) + 1, 0x09)) + name
        )

    def scanner(self):
        self.ble.gap_scan(SCAN_DURATION, 500000, 11250, True)

    def connect_nrf(self, addr_type=None, addr=None):
        """BLE.gap_connect(addr_type, addr, scan_duration_ms=2000,)"""
        print(f"Trying to esablish connection to nrf with addr {addr}")
        self._addr_type = addr_type or self._addr_type
        self._addr = addr or self._addr
        if self._addr_type is None or self._addr is None:
            return False
        self.ble.gap_connect(self._addr_type, self._addr)
        return True

    # Disconnect from current device.
    def disconnect(self):
        if not self._conn_handle:
            return
        self.ble.gap_disconnect(self._conn_handle)
        self._reset()


# test
ble = BLE("ESP32")
