import time
import board
import neopixel
import adafruit_ble
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService

# Initialize the BLE radio and UART service.
ble = adafruit_ble.BLERadio()
uart_server = UARTService()
advertisement = ProvideServicesAdvertisement(uart_server)

# Initialize the NeoPixel object.
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.3, auto_write=False)

# Set the colors to be used for the NeoPixel.
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 140, 0)
PURPLE = (128, 0, 128)
PINK =(255, 20, 147)
GOLD = (255, 215, 0)


while True:
    # Advertise when not connected.
    ble.start_advertising(advertisement)
    # Wait until a connection is established.
    while not ble.connected:
        pass
    # Connection has been established. Stop advertising.
    ble.stop_advertising()
    while ble.connected:
        # Check if there is any incoming data on the UART service.
        if uart_server.in_waiting:
            # Read the incoming data.
            data = uart_server.read(uart_server.in_waiting)
            print("Received: ", data)
            # Check if the data matches any of the predefined commands.
            if data == b'on\n':
                # Turn the NeoPixel white.
                pixel.fill(WHITE)
                pixel.show()
            elif data == b'off\n':
                # Turn the NeoPixel off.
                pixel.fill(0)
                pixel.show()
            elif data == b'flash\n':
                # Flash the NeoPixel 10 times.
                for i in range(10):
                    pixel.fill(WHITE)
                    pixel.show()
                    time.sleep(0.5)
                    pixel.fill(0)
                    pixel.show()
                    time.sleep(0.5)
            elif data == b'red\n':
                # Set the NeoPixel to red.
                pixel.fill(RED)
                pixel.show()
            elif data == b'green\n':
                # Set the NeoPixel to green.
                pixel.fill(GREEN)
                pixel.show()
            elif data == b'blue\n':
                # Set the NeoPixel to blue.
                pixel.fill(BLUE)
                pixel.show()
            elif data == b'yellow\n':
                # Set the NeoPixel to yellow.
                pixel.fill(YELLOW)
                pixel.show()
            elif data == b'orange\n':
                # Set the NeoPixel to orange.
                pixel.fill(ORANGE)
                pixel.show()
            elif data == b'purple\n':
                # Set the NeoPixel to purple.
                pixel.fill(PURPLE)
                pixel.show()
            elif data == b'pink\n':
                # Set the NeoPixel to pink.
                pixel.fill(PINK)
                pixel.show()
            elif data == b'gold\n':
                # Set the NeoPixel to gold.
                pixel.fill(GOLD)
                pixel.show()
            elif data == b'flash_all\n':
                # Flash all the colors in the list.
                colors = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE, PINK, GOLD]
                while True:
                    for color in colors:
                        pixel.fill(color)
                        pixel.show()
                        time.sleep(1)
                        # Check if the user has sent a any other command.
                        if uart_server.in_waiting:
                            break
                    if uart_server.in_waiting:
                        break
            else:
                # Unknown command received.
                print("Unknown command")
            # Wait a small amount of time before checking for more incoming data.
            time.sleep(0.1)
        # Wait a small amount of time before checking for a connection again.
        time.sleep(0.1)
    # Connection has been lost. Print a message and wait a small amount of time.
    print("Disconnected")
    time.sleep(0.1)
