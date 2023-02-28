from machine import Pin, ADC, PWM
from time import sleep

led_pin = Pin(13)
pot_pin = 0

led = PWM(led_pin, 5000)
pot = ADC(pot_pin)

pot_deger = 0
sleep_second = 1

while True:
    pot_deger = pot.read()
    led.duty(pot_deger)

    sleep(sleep_second)