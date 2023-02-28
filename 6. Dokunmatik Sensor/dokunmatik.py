from machine import Pin
from time import sleep

touchSensor_Pin = 5
touch_sensor = Pin(touchSensor_Pin, Pin.IN)

isTouch = 0
touch_second = 1

while True:
    isTouch = touch_sensor.value()
    sleep(touch_second)
    
    if isTouch == True:
        print("Temas var.")
    else:
        print("Temas yok.")