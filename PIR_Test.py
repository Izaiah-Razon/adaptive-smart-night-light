from machine import Pin
import time

pir = Pin(14, Pin.IN)

print("Warming up PIR...")
time.sleep(20)
print("Ready")

while True:
    print("Motion:", pir.value())
    time.sleep(0.2)