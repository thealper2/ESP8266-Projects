from machine import ADC
from time import sleep

pot_pin = 0
pot = ADC(pot_pin)

pot_deger = 0
sleep_second = 1

while True:
    pot_deger = pot.read()
    print("Potansiyometre degeri: ", pot_deger)
    sleep(sleep_second)