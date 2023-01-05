# Instructions to run the project locally

We have created a project to display the temperature, humidity and location read by Adafruit Feather Bluefruit Sense(nRF52480), on Adafruit FeatherWing 128x32 OLED display which is connected to Adafruit HUZZAH32 - ESP32 Feather. ESP32 and nRF52480 are connected over bluetooth.
 
## Device Requirements:
1. Breadboard
2. Adafruit HUZZAH32 - ESP32 Feather
2. Adafruit Feather Bluefruit Sense(nRF52480)
3. Two USB cables
4. Adafruit FeatherWing 128x32 OLED

## Setup the connection:
1. Fix the ESP32 and nRF52480 on breadboard for convinience.
2. Connect the ESP32 to your PC using an USB cable
3. Insert the OLED on top of ESP32
4. Connect the nRF52480 to another PC using an USB cable

## Software requirements
1. Flash Micropython on ESP32
2. Save the ssd1306 module one the ESP32 device. Find the link to ssd1306.py module here - https://github.com/micropython/micropython-lib/blob/master/micropython/drivers/display/ssd1306/ssd1306.py
Setup 
2. CircuitPython on Adafruit Featherwing Bluefruit Sense(nRF452480) by following the steps given at https://learn.adafruit.com/adafruit-feather-sense/circuitpython-on-feather-sense
3. Open the usb directory inside visual studio code
4. Go to View->Command Palette menu, select the board using command > "CircuitPython: choose CircuitPython Board" and select "Adafruit Industries LLC: Feather Bluefruit Sense"
Install the libraries: type the command > "CircuitPython: Show available libraries", then search for libraries "adafruit_sht31d" and install. Similarly search for "adafruit_ble" and install. The libraries will be downloaded in the lib folder.

## Download the project
1. Download the files ble_advertising.py and tempRead.py and upload it to ESP32
2. Download the file uart_nrf52480-2.py on nRF52480 device.

## Run the Project
1. Run the uart_nrf52480-2.py on nRF52480 device. The device starts bluetooth and starts advertising to connect to the central device.
2. Run the tempRead.py on the ESP32. The device starts running and tries to establish connection to the nRF52480. 
3. When the connection is established between both the device, you can see "connection established" on the nRF52480 console .

