from machine import Pin
from time import sleep

def nothing(x):
    pass

buton_pin = 5
kirmiziLed_pin = 4
yesilLed_pin = 0
maviLed_pin = 2
sleep_second = 1

buton = Pin(buton_pin, Pin.IN)
butonDurum = 0
sayac = 0

kirmiziLed = Pin(kirmiziLed_pin, Pin.OUT, value=0)
yesilLed = Pin(yesilLed_pin, Pin.OUT, value=0)
maviLed = Pin(maviLed_pin, Pin.OUT, value=0)
    
buton.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=callback)

while True:
    kirmiziLed_pin.on()
    sleep(sleep_second)
    kirmiziLed_pin.off()
    sleep(sleep_second)