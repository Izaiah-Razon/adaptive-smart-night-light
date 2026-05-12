from machine import Pin, ADC, PWM
import time

# -----------------------------
# Pin Setup
# -----------------------------

light_sensor = ADC(26)      # Photoresistor on GP26 / ADC0
brightness_knob = ADC(27)   # Potentiometer on GP27 / ADC1
pir_sensor = Pin(14, Pin.IN)

led = PWM(Pin(15))
led.freq(1000)

# -----------------------------
# Settings
# -----------------------------

DARK_THRESHOLD = 25000
OFF_DELAY_SECONDS = 30

last_motion_time = 0
light_on = False


def read_average_adc(sensor, samples=10):
    total = 0
    for _ in range(samples):
        total += sensor.read_u16()
        time.sleep(0.01)
    return total // samples


def set_led_brightness(value):
    led.duty_u16(value)


def turn_off_led():
    set_led_brightness(0)


print("Adaptive Smart Night Light Started")
print("Waiting for PIR sensor to warm up...")
time.sleep(10)
print("System ready.")

while True:
    light_value = read_average_adc(light_sensor)
    knob_value = brightness_knob.read_u16()
    motion_detected = pir_sensor.value()

    room_is_dark = light_value < DARK_THRESHOLD

    if motion_detected == 1:
        last_motion_time = time.time()

    time_since_motion = time.time() - last_motion_time

    if room_is_dark and time_since_motion <= OFF_DELAY_SECONDS:
        set_led_brightness(knob_value)
        light_on = True
    else:
        turn_off_led()
        light_on = False

    print(
        "Light ADC:", light_value,
        "| Knob:", knob_value,
        "| Motion:", motion_detected,
        "| Dark:", room_is_dark,
        "| LED On:", light_on
    )

    time.sleep(0.2)