from machine import Pin 
from time import sleep

touchSensor_pin = 5
ledPin = 4

touch_sensor=Pin(touchSensor_pin,Pin.IN)
led =Pin(ledPin, Pin.OUT, value=0)

isTouch = 0
touch_second = 1


while True:
    isTouch = touch_sensor.value()
    sleep(touch_second = 1)
  
    if isTouch == True:
        led.value(1)
    else:
        led.value(0)
    