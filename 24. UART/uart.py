from machine import UART
from time import sleep

uart = UART(1, baudrate=9600)
sleep_second = 1

while True:
    uart.write("UART CONNECTION...\n")
    sleep(1)