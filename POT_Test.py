from machine import ADC
import time

pot = ADC(27)

while True:
    value = pot.read_u16()
    print(value)
    time.sleep(0.2)