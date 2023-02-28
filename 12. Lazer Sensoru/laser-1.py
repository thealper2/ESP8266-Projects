from machine import Pin
from time import sleep

laser_pin = 5
sleep_second = 1

laser = Pin(laser_pin, Pin.OUT)

while True:
	laser.on()
	sleep(sleep_second)
	laser.off()
	sleep(sleep_second)