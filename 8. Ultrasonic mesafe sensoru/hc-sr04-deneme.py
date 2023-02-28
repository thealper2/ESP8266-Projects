from machine import Pin, Timer
from time import sleep
from hcsr04 import HCSR04 

trigger_pin = 5
echo_pin = 4
led_pin = 0
sleep_second = 1000

ultrasonic = HCSR04(trigger_pin=trigger_pin, echo_pin=echo_pin, echo_timeout_us=1000000)
led = Pin(led_pin, Pin.OUT)

while True:
    mesafe = ultrasonic.distance_cm()
    print('Uzaklik: ', mesafe, 'cm')

    if int(mesafe) <= 20:
        led.value(1)
    else:
        led.value(0)
        
    sleep(sleep_second)
