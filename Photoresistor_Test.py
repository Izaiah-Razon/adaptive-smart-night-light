from machine import ADC
import time

light = ADC(26)

while True:
    print(light.read_u16())
    time.sleep(0.2)