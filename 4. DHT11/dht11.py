from dht import DHT11
from machine import Pin
from time import sleep

dhtPin = Pin(5)
dht_second = 1

dht_sensor = DHT11(dhtPin)

while True:
    dht_sensor.measure()
    print("Sicaklik:", dht_sensor.temperature())
    print("Nem:", dht_sensor.humidity())
    sleep(dht_second)