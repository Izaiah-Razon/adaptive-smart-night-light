from machine import Pin, PWM
import time

led = PWM(Pin(15))
led.freq(1000)

while True:
    led.duty_u16(0)
    time.sleep(1)

    led.duty_u16(15000)
    time.sleep(1)

    led.duty_u16(40000)
    time.sleep(1)

    led.duty_u16(65000)
    time.sleep(1)