import machine
led = machine.Pin(13,machine.Pin.OUT)
led.off()

# ************************
# Configure our ESP32 wifi as Station mode
import network

station = network.WLAN(network.STA_IF)
if not station.isconnected():
    print('Please wait, connecting to the network.....')
    station.active(True)
    #station.connect('your wifi name', 'your wifi password')
    station.connect('SFR-5a88', 'DUXZF2G2WYGZ')
    while not station.isconnected():
        pass
print('Network configuration:', station.ifconfig())
print('Copy the first IP address displayed above & paste it on your browser\'s search bar [don\'t forget to hit \'Enter\' key]')

# ************************
# Configure the socket connection over TCP/IP
import socket

sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET - use Internet Protocol v4 addresses
# SOCK_STREAM means that it is a TCP socket
sockt.bind(('',80)) # specifies that the socket is reachable by any address the machine happens to have                 
sockt.listen(5)     # max of 5 socket connections

# ************************
# Function for creating the web page (front-end)
def web_page():
    if led.value() == 1:
        led_state = 'ON'
        print('LED is ON')
    elif led.value() == 0:
        led_state = 'OFF'
        print('LED is OFF')

    html_page = """   
      <html>   
      <head>   
       <meta content="width=device-width, initial-scale=1" name="viewport"></meta>   
      </head>   
      <body>   
        <center><h1>Welcome!</h1></center>
        <center><h2>ESP32 Web Server in MicroPython</h2></center>   
        <center>   
         <form>   
          <button name="LED" type="submit" value="1"> LED ON </button>   
          <button name="LED" type="submit" value="0"> LED OFF </button>   
         </form>   
        </center>   
        <center><p>The GPIO-LED is now <strong>""" + led_state + """</strong></p></center>   
      </body>   
      </html>"""  
    return html_page   

while True:
    # Socket accept() 
    conn, addr = sockt.accept()
    print("Got connection from %s" % str(addr))
    
    # Socket receive()
    request=conn.recv(1024)
    print("")
    print("")
    print("Content %s" % str(request))

    # Socket send()
    request = str(request)
    led_on = request.find('/?LED=1')
    led_off = request.find('/?LED=0')
    if led_on == 6:
        print('LED ON')
        print(str(led_on))
        led.value(1)
    elif led_off == 6:
        print('LED OFF')
        print(str(led_off))
        led.value(0)
    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    
    # Socket close()
    conn.close()


