import time
import board
import digitalio
from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService

# Set up the BLE radio
ble = BLERadio()

# Create a UART service for communication
uart_service = UARTService()

# Set up the advertisement
advertisement = ProvideServicesAdvertisement(uart_service)

# Start advertising
ble.start_advertising(advertisement)
print("Advertising BLE server...")

# Wait for a connection
while not ble.connected:
    time.sleep(0.1)

# Connection has been established
print("BLE connection established!")

# After connection is established, wait until data is received before sending data
while ble.connected:
    # Read data from the UART service
    data = uart_service.read()
    if data:
        print(f"Received data: {data}")

        # Write data to the UART service
        uart_service.write(b'Hello from CircuitPython!')

# Stop advertising
ble.stop_advertising()
print("Stopped advertising BLE server")







































#import time
#import board
#import digitalio
#from adafruit_ble import BLERadio
#from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
#from adafruit_ble.services.nordic import UARTService

# Set up the BLE connection
ble = BLERadio()

# Scan for BLE peripherals
#print("Scanning for BLE peripherals...")
#while not ble.connected:
    #for device in ble.start_scan(ProvideServicesAdvertisement, timeout=5):
        #if device.complete_name == "Dann":
            #print(f"Connecting to {device.complete_name}...")
            #ble.connect(device)
            #break

# Create a UART service for communication
#uart_service = UARTService()

# Read data from the UART service
#data = uart_service.read()
#print(f"Received data: {data}")

# Write data to the UART service
#uart_service.write(b'Hello from CircuitPython!')

