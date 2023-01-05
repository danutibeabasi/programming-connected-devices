# NeoPixel Bluetooth Control

This code allows you to control a NeoPixel LED connected to your CircuitPython device through a Bluetooth connection.

## Prerequisites
You will need the following libraries:
- board
- neopixel
- adafruit_ble

## Setup
Connect your NeoPixel LED to your CircuitPython device according to the NeoPixel 

## Documentation.
- Make sure that your CircuitPython device is paired with a device that supports Bluetooth Low Energy (BLE) such as a smartphone or a computer.
Modify the board.NEOPIXEL pin in the code to match the pin where you have connected your NeoPixel LED.
- Upload the code to your CircuitPython device.

## Usage
- Make sure that your CircuitPython device is turned on and that it is within range of your BLE device.
- Connect to the CircuitPython device using your BLE device. The name of the device will be "CircuitPython UART".
- Once connected, you can send the following commands to control the NeoPixel LED:
  
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
| flash_all     | Flash the NeoPixel LED with all the colors in the list.       |
| rainbow       | Set the NeoPixel LED to a rainbow of colors.                  |


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

To set the NeoPixel LED to a rainbow of colors, send the following string over the UART service:

```
rainbow\n
```

## Additional Information
You can customize the colors used in the code by modifying the RED, GREEN, BLUE, WHITE, YELLOW, ORANGE, PURPLE, PINK, and GOLD variables at the beginning of the code. You can also add additional colors to the colors list in the flash_all command.

You can change the brightness of the NeoPixel LED by modifying the brightness parameter in the neopixel.NeoPixel object. The value should be a float between 0 and 1, where 0 is off and 1 is maximum brightness.

You can modify the duration of the flash by modifying the time.sleep() function calls in the flash and flash_all commands. The value is in seconds.