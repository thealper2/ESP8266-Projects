import socket
from network import WLAN
from esp import osdebug
from gc import collect    
from machine import Pin

osdebug(None)
collect()

ssid = 'WIFI_SSID'    
password = 'WIFI_PASS'

station = WLAN(network.STA_IF)    

station.active(True)
station.connect(ssid, password)     

while station.isconnected() == False:
    pass

print("IFCONFIG: ", station.ifconfig())

led_pin = 5
led = Pin(led_pin, Pin.OUT)

def web_site():
    html = """<html>
                <head>
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                </head>
                <body>
                    <h1>ESP8266 ile Led Yakma</h1>
                    <a href=\"?led=acik\"><button>LED AC</button></a>
                    <br>
                    <a href=\"?led=kapali\"><button>LED KAPAT</button></a>
                </body>
              </html>"""
    return html

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #server'ı dinlemeye başladık. 
server_port = 80
server.bind(('', server_port))
listen_second = 5
server.listen(listen_second)

while True:
    conn, addr = server.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    print('Content = %s' % str(request))
    
    request = str(request)
    led_ac = request.find('/?led=acik')
    led_kapat = request.find('/?led=kapali')
    if led_ac == 6:
        led.value(1)
    if led_kapat == 6:
        led.value(0)
    
    response = web_site()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()
