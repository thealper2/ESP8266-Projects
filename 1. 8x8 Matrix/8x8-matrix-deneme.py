from max7219 import Matrix8x8
from machine import Pin, SPI

spi = SPI(1, baudrate=10000000, polarity=1, phase=0)
matrixPin = Pin(5)


matrix = Matrix8x8(spi, matrixPin, 1)
matrix.brightness(10)
matrix.fill(0)
matrix.text('A', 0, 0)
matrix.show()
