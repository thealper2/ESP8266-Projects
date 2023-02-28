from machine import Pin, I2C
from sh1106 import SH1106_I2C

sda_pin = Pin(5)
scl_pin = Pin(4)

WIDTH = 128
HEIGHT = 64

i2c = I2C(sda=sda_pin, scl=scl_pin)

oled = SH1106_I2C(WIDTH, HEIGHT, i2c)
oled.text('MicroPython', 0, 0)
oled.show()