# Adaptive Smart Night Light

## Project Overview

The Adaptive Smart Night Light is a Raspberry Pi Pico W project that turns on an LED only when the room is dark and motion is detected. The goal of the project is to make a night light that responds to the environment instead of staying on all the time.

This project uses a photoresistor to measure ambient light, a PIR motion sensor to detect movement, a potentiometer to adjust brightness, and PWM to control the LED.

## Team Members

- Izaiah Razon
- Dillon Catlett

## Features

- Detects room brightness using a photoresistor
- Detects movement using a PIR motion sensor
- Lets the user adjust LED brightness with a potentiometer
- Uses PWM to control LED brightness
- Automatically turns off after no recent motion is detected
- Uses separate test programs for each component

## Hardware Used

- Raspberry Pi Pico W
- Breadboard
- Jumper wires
- Photoresistor
- 10k resistor
- Potentiometer
- PIR motion sensor
- LED
- 330 ohm resistor

## Pin Connections

| Component | Pico W Pin |
|---|---|
| Photoresistor voltage divider | GP26 |
| Potentiometer middle pin | GP27 |
| PIR motion sensor OUT | GP14 |
| LED PWM signal | GP15 |
| Sensor power | 3V3(OUT) |
| Ground | GND |
