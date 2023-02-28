from machine import Pin
from time import sleep

led_pin = 5
led = Pin(led_pin, Pin.OUT)

sleep_second = 1

while True:
    led.value(0)
    sleep(sleep_second)

    led.value(1)
    sleep(sleep_second)