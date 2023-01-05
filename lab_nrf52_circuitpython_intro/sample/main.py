import time
import board
import adafruit_sht31d
import adafruit_ble
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService

# Initialize the BLE radio and UART service.
ble = adafruit_ble.BLERadio()
uart_server = UARTService()
advertisement = ProvideServicesAdvertisement(uart_server)

# Initialize the SHT31D sensor.
i2c = board.I2C()
sht31d = adafruit_sht31d.SHT31D(i2c)

while True:
    # Advertise when not connected.
    ble.start_advertising(advertisement)
    # Wait until a connection is established.
    while not ble.connected:
        pass
    # Connection has been established. Stop advertising.
    ble.stop_advertising()
    while ble.connected:
        # Read the temperature and humidity from the SHT31D sensor.
        temperature = sht31d.temperature
        humidity = sht31d.relative_humidity
        # Get the current time and location.
        #current_time = time.localtime())
        location = "Saint Etienne, France"
        # Format the data as a string.
        data = f"Temperature: {temperature:.1f} C\nHumidity: {humidity:.1f}\nLocation: {location}\n"
        # Send the data over the UART service.
        uart_server.write(data)
        # Wait before sending the next data.
        time.sleep(10)

