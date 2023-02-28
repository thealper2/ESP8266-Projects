from machine import Pin, I2C
from sh1106 import SH1106_I2C
from dht import DHT11
from time import sleep

dht_pin = Pin(0)
sda_pin = 5
scl_pin = 4

WIDTH = 128
HEIGHT = 64
sleep_second = 1

dhtt = DHT11(dht_pin)

i2c = I2C(sda=sda_pin, scl=scl_pin)
oled = SH1106_I2C(WIDTH, HEIGHT, i2c)

while True:
    dhtt.measure()
    sleep(sleep_second)

    sicaklik = dhtt.temperature()
    nem = dhtt.humidity()

    oled.fill(0)
    oled.text("Sicaklik:", 0, 0)
    oled.text(str(sicaklik), 90, 0)
    oled.text("Nem:", 0, 40)
    oled.text(str(nem), 60, 10)

    oled.show()