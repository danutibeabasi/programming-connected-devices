# from machine import Pin

# p13 = Pin(13, Pin.OUT)

# p13.value(0)
# p13.value(1)


# p27 = Pin(27, Pin.IN, Pin.PULL_UP)

# print(p27.value())

# p13.init(p13.IN, p13.PULL_DOWN)

# # def toggle(p):
# #     p.value(not p.value())
       
    
# p27.irq(trigger = Pin.IRQ_FALLING, handler = lambda p27:p27.value(not p27.value()))



# Demonstrate the voltage measured on GPIO#27 should range between 0V and 1750mV

from machine import Pin, ADC, UART
import time

p27 = Pin(27, Pin.IN)

adc = ADC(p27)
uart0 = UART(0, baudrate=9600, tx=33, rx=32)
while True:
    uart0.write(adc.read_uv())
    time.sleep_ms(100)
