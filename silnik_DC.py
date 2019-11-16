import RPi.GPIO as GPIO
import time


class SilnikDC:
    def __init__(self, channel):

        self.channel = channel
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.channel, GPIO.OUT)  # , initial=GPIO.HIGH)
        self.silnikDC = GPIO.PWM(self.channel, 50)
        self.silnikDC.start(0)
