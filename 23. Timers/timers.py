from machine import Pin, Timer
from time import sleep

led_pin = 5
led = Pin(led_pin, Pin.OUT)

sleep_second = 1
period_second = 10000

timer = Timer(-1)
timer.init(period=period_second, mode=Timer.PERIODIC, callback=lambda x:led.value(not led.value()))

while True:
    print("...")
    sleep(sleep_second)