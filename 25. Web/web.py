import socket
from network import WLAN
from esp import osdebug
from gc import collect    

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

def web_site():
    html = """<html>
                <head>
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                </head>
                <body>
                    <h1>Hello World!</h1>
                </body>
              </html>"""
    return html

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server_port = 80
server.bind(('', server_port))

listen_second = 5
server.listen(listen_second)

while True:
    conn, addr = server.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    print('Content = %s' % str(request))
    response = web_site()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()