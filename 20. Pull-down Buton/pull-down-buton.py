from machine import Pin
from time import sleep

buton_pin = 5
led_pin = 4

buton = Pin(buton_pin, Pin.IN)
led = Pin(led_pin, Pin.OUT, value=0)

butonDurumu = 0 
sleep_second = 1

while True:
    butonDurumu = buton.value()
    
    if butonDurumu == True:
        led.on()
    else:
        led.off()

    sleep(1)