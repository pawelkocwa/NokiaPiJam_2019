import RPi.GPIO as GPIO
import time


class Serwo():
    def __init__(self, channel):

        self.channel = channel
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.channel, GPIO.OUT)  # , initial=GPIO.HIGH)
        self.serwo = GPIO.PWM(self.channel, 50)
        self.serwo.start(0)

        # podnieś serwo, żeby nie popisać przez przypadek.
        self.serwo_up()


    def set_fullfill(self, new_fullfill):
        self.serwo.ChangeDutyCycle(new_fullfill)
        print("Zmieniono wypełnienie na : " +  str(new_fullfill))

    def serwo_up(self):
        self.set_fullfill(8)
        print("Serwo zostało podniesione")

    def serwo_down(self):
        self.set_fullfill(3)
        print("Serwo zostało opuszczone")
