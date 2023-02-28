from machine import Pin, PWM
from time import sleep_ms

led_pin = Pin(4)
led = PWM(led_pin, freq=1000)

while True:
    for i in range(0, 1000):
        led.duty(i)
        sleep_ms(500)