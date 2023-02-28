from machine import Pin
from time import sleep

kirmiziLed_pin = 5
yesilLed_pin = 4
maviLed_pin = 0
sariLed_pin = 2
sleep_second = 1

kirmiziLed = Pin(kirmiziLed_pin, Pin.OUT, value=0)
yesilLed = Pin(yesilLed_pin, Pin.OUT, value=0)
maviLed = Pin(maviLed_pin, Pin.OUT, value=0)
sariLed = Pin(sariLed_pin, Pin.OUT, value=0)

ledler = [kirmiziLed, yesilLed, maviLed, sariLed]

while True:
    for led in range(0, 4):
        ledler[led].on()
        sleep(sleep_second)

        ledler[led].off()
        sleep(sleep_second)
