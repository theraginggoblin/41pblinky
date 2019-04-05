import RPi.GPIO as GPIO
import time

led_pin = 10

def pin_setup():
    GPIO.setup(led_pin, GPIO.OUT)

def led_on():
    GPIO.output(led_pin, GPIO.HIGH)

def led_off():
    GPIO.output(led_pin, GPIO.LOW)

def led_blink(milliseconds):
    led_on()
    time.sleep(milliseconds)
    led_off()

try:
    while 1:
        led_blink(250)
        time.sleep(0.25)
except KeyboardInterrupt:
    GPIO.cleanup()
