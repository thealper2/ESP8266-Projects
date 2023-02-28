import socket
from network import WLAN
from esp import osdebug
from gc import collect    
from machine import Pin
from dht import DHT11

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

dht_pin = Pin(4)
dhtt = DHT11(dht_pin)

sicaklik = 0
nem = 0

dhtt.measure()
temp = dhtt.temperature()
hum = dhtt.humidity()
    
def web_page():
    html = """<html>
                <head>
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                </head>
                <body>
                    <h1>DHT11 Sensor</h1>
                    <p>Sicaklik:""" + str(temp) + """</p>
                    <p>Nem:""" + str(hum) + """</p>
                </body>
              </html>"""
    return html

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_port = 80
server.bind(('', 80))
listen_second = 5
server.listen(5)

while True:
    conn, addr = server.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    print('Content = %s' % str(request))
    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()