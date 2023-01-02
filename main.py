from machine import UART, deepsleep

uart1 = UART(1, baudrate=9600, tx=33, rx=32)

while True:
    uart1.write('hello')  # write 5 bytes
    deepsleep(10000)
#uart1.read(5) 