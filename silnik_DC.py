import RPi.GPIO as GPIO
import time


class SilnikDC:
    def __init__(self, dir_channel, step_channel, ID):

        self.ID = ID

        self.dir_channel = dir_channel
        self.step_channel = step_channel

        self.STOP_var = False
        self.DIR_var = 0
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.dir_channel, GPIO.OUT)  # , initial=GPIO.HIGH)
        GPIO.setup(self.step_channel, GPIO.OUT)  # , initial=GPIO.HIGH)
        
        
         

    def STOP(self):
        # stop dla silnika!
        self.STOP_var = True


    def hope(self, home_angle_for_DC):

        pass

    def one_step(self):
        """
        
        :param dir: jeśli dir jest 1 to ruszamy się w prawo, jeśli jest 0 to ruszamy w lewo 
        :return: 
        """

        if self.DIR_var == 1:
            GPIO.output(self.dir_channel, GPIO.HIGH)
        elif self.DIR_var == 0:
            GPIO.output(self.dir_channel, GPIO.LOW)

        if self.STOP_var:
            self.DIR_var = 0
            self.STOP_var = False
            pass
        else:
            GPIO.output(self.step_channel, GPIO.LOW)
            # time.sleep(0.001)
            GPIO.output(self.step_channel, GPIO.HIGH)
            # time.sleep(0.001)
            GPIO.output(self.step_channel, GPIO.LOW)

    def __str__(self):
        print("SILNIK "+ str(self.ID)+ " STOP: " + str(self.STOP_var))