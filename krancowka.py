import RPi.GPIO as GPIO

class Krancowka:
    def __init__(self, channel, number_of_krancowka):
        
        self.channel = channel
        self.ID = number_of_krancowka

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.channel, GPIO.IN, GPIO.PUD_UP)  # mamy resystor podciągający
        # self.krancowka = GPIO.PWM(self.channel, 50)
        # self.krancowka.start(0)

    def check_state(self):
        current_state = GPIO.input(self.channel)
        print("Obecny stan krancowki numer: "+ str(self.ID) + " to: " + str(current_state))
        return current_state

    def STOP(self):
        if self.check_state() == 0:
            return True
        else:
            return False