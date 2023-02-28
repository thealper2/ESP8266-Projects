from machine import Pin
from time import sleep

buzzerPin = 5
sleep_second = 1

buzzer = Pin(buzzerPin, Pin.OUT, value=0)

while True:
    buzzer.on()
    sleep(sleep_second)
    buzzer.off()
    sleep(sleep_second)
    buzzer.on()