from machine import Pin
from time import sleep

buton_pin = 5
kirmiziLed_pin = 4
yesilLed_pin = 0
maviLed_pin = 2

buton = Pin(buton_pin,Pin.IN)
kirmiziLed = Pin(kirmiziLed_pin,Pin.OUT, value=0)
yesilLed = Pin(yesilLed_pin,Pin.OUT, value=0)
maviLed = Pin(maviLed_pin,Pin.OUT, value=0)

butonDurumu = 0
sayac = 0
sleep_second = 1

while True:
    butonDurumu = buton.value()
    
    if butonDurumu == True:
        sayac += 1
    
    if sayac % 3 == 1:
        kirmiziLed.on()
        yesilLed.off()
        maviLed.off()

    elif sayac % 3 == 2:
        kirmiziLed.off()
        yesilLed.on()
        maviLed.off()

    elif sayac % 3 == 0:
        kirmiziLed.off()
        yesilLed.off()
        maviLed.on()

    sleep(sleep_second)
