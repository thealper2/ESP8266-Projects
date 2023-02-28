from machine import ADC, Pin
from time import sleep

ldr_pin = 0
led_pin = 5

ldr = ADC(ldr_pin)
led = Pin(led_pin, Pin.OUT, value=0)

ldr_deger = 0
sleep_second = 1

while True:
    ldr_deger = ldr.read()
    print("İsik degeri:", ldr_deger)
    sleep(sleep_second)

    if ldr_deger >= 700:
        led.on()
    else:
        led.off()