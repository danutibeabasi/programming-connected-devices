# NeoPixel Bluetooth Control

This code allows you to control a NeoPixel LED connected to your CircuitPython device through a Bluetooth connection.
## Device requirements
- Adafruit Feather Bluefruit Sense(nRF52480)
- mobile phone

## Prerequisites
You will need the following libraries:
- board
- neopixel
- adafruit_ble

## Setup nRF52480
1. Download the file code.py from the folder - "lab_nrf52_circuitpython_intro\Neon-pixel-bluetooth-control"
2. Upload the code.py to your Adafruit Feather Bluefruit Sense(nRF52480)  
3. Modify the board.NEOPIXEL pin in the code to match the pin where you have connected your NeoPixel LED.
4. Run the code.py on the nRF52480 device and setup the Bluetooth connect application on your mobile phone

## On your mobile phone
1. Download the Bluefruit connect application from playstore. 
2. Enable bluetooth on your mobile phone. 
3. Make sure that your CircuitPython device is turned on and that it is within range of your BLE device.
4. Search for the "CIRCUITPY" device on the application(the nRF52480 should be running the bluetooth) and connect to it. 
5. Open "UART" mode and start sending commands listed above.


  
## Command Reference

| Command       | Description                                                  |
|---------------|--------------------------------------------------------------|
| on            | Turn the NeoPixel LED white.                                 |
| off           | Turn the NeoPixel LED off.                                    |
| flash         | Flash the NeoPixel LED 10 times.                              |
| red           | Set the NeoPixel LED to red.                                  |
| green         | Set the NeoPixel LED to green.                                |
| blue          | Set the NeoPixel LED to blue.                                 |
| yellow        | Set the NeoPixel LED to yellow.                               |
| orange        | Set the NeoPixel LED to orange.                               |
| purple        | Set the NeoPixel LED to purple.                               |
| pink          | Set the NeoPixel LED to pink.                                 |
| gold          | Set the NeoPixel LED to gold.                                 |
| flash_all     | Flash the NeoPixel LED with all the colors in the list.       |                  |


## Example
To turn the NeoPixel LED red, send the following string over the UART service:

```
red\n
```

To turn the NeoPixel LED off, send the following string over the UART service:

```
off\n
```
To flash the NeoPixel LED 10 times, send the following string over the UART service:
```
flash\n
```
To flash the NeoPixel LED with all the colors in the list, send the following string over the UART service:

```
flash_all\n
```


## Additional Information
You can customize the colors used in the code by modifying the RED, GREEN, BLUE, WHITE, YELLOW, ORANGE, PURPLE, PINK, and GOLD variables at the beginning of the code. You can also add additional colors to the colors list in the flash_all command.

You can change the brightness of the NeoPixel LED by modifying the brightness parameter in the neopixel.NeoPixel object. The value should be a float between 0 and 1, where 0 is off and 1 is maximum brightness.

You can modify the duration of the flash by modifying the time.sleep() function calls in the flash and flash_all commands. The value is in seconds.

