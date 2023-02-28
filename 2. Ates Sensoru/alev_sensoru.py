from time import sleep
from machine import Pin, ADC

flamePin = 0
ledPin = 5
flame_count = 0
flame_second = 1

flame = ADC(flamePin)
led = Pin(ledPin, Pin.OUT, value=0)

while True:
    flame_count = flame.read()
    print("Flame sensor: ", flame_count)    
    sleep(flame_second)
    
    if flame_count < 50:
        print("ATES ALGILANDI !..")
        led.value(1)
    else:
        led.value(0)