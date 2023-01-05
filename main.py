from machine import Pin, SoftI2C
import ssd1306
import framebuf
import time
import dht


d = dht.DHT22(Pin(27))

i2c = SoftI2C(sda=Pin(23), scl=Pin(22))
display = ssd1306.SSD1306_I2C(128, 64, i2c)
display.poweron()
currentTemperature = ''
currentHumidity = ''
while True:
    d.measure()
    temperature = d.temperature()
    humidity = d.humidity()
    print("Temperature: %0.1f C" % temperature)
    print("Humidity: %0.1f %%" % humidity)
    # for t in time.gmtime():
    #     currenttime = currenttime + str(t)
    #print(currenttime)
    display.text(str(temperature), 2, 2, 1)
    display.text(str(humidity), 6, 6, 1)
    display.show()
    time.sleep(2)