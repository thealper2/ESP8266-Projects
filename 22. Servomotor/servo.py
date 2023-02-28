from machine import Pin, PWM
from time import sleep

servo_pin = Pin(4)
servo = PWM(servo_pin, freq=50)

acilar = [30, 60, 90]
sleep_second = 1

while True:
    for aci in range(0,3):
        servo.duty(aci)
        sleep(sleep_second)