# Temperature and Humidity BLE Reader
This code allows a device with a BLE radio and an SHT31D sensor to send temperature and humidity data to a connected device over a BLE connection. The temperature and humidity data is read from the SHT31D sensor at intervals of 10 seconds and is sent over the BLE connection using a UART service.

## Prerequisites
To use this code, you will need:

- A device with a BLE radio (e.g. a microcontroller with built-in BLE capability or a BLE module)
- An SHT31D temperature and humidity sensor
- A device to receive the temperature and humidity data (e.g. a smartphone)

You will also need to install the following libraries:
- adafruit_ble
- adafruit_sht31d
  
## Usage


- Upload the code to your device.

- On your receiving device, scan for BLE devices and connect to the device running the code.
- The temperature and humidity data will be sent at intervals of 10 seconds.
  
## Troubleshooting
- If you are unable to establish a BLE connection, check that your device has BLE capability and that it is turned on.
- If you are unable to read data from the SHT31D sensor, check that the sensor is connected correctly and that the correct libraries have been installed.
  
## Additional Notes
The temperature and humidity data is formatted as a string before being sent over the UART service. The string includes the temperature in degrees Celsius, the humidity as a percentage, and the current location. The location is currently hardcoded as "Saint Etienne, France" in the code. You can update this to reflect the actual location of your device.