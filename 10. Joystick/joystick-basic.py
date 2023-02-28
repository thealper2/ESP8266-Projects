from machine import Pin, ADC
from time import sleep

buton_pin = 5
x_pin = Pin(4)
y_pin = Pin(0)
sleep_second = 1

aX = ADC(x_pin)
aY = ADC(y_pin)

buton = Pin(buton_pin, Pin.IN, Pin.PULL_UP)

while True:
    x_pos = xAxis.read_u16()
    y_pos = yAxis.read_u16()
    butonDegeri = buton.value()

    print("---------------")
    print("X:", str(x_pos))
    print("Y:", str(y_pos))
    print("Buton:", str(butonDegeri))
    print("---------------")
    
    sleep(sleep_second)