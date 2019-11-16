import RPi.GPIO as GPIO
import time

from krancowka import Krancowka
from serwo import Serwo
from silnik_DC import SilnikDC

KANAL_KRANCOWKA_X = 36	# wyzej os x
KANAL_KRANCOWKA_Y = 38 	# nizej os y

KANAL_SILNIK_DC_X = 21	# ten wyzej to X
KANAL_SILNIK_DC_Y = 22	# ten nizej to Y

KANAL_SERWO = 12




def main():
	# stworzenie instancji Serwa
	# serwo = Serwo(KANAL_SERWO)

	# tworzenie isntancji krańcówek:
	krancowka_X = Krancowka(KANAL_KRANCOWKA_X, 1)
	krancowka_Y = Krancowka(KANAL_KRANCOWKA_Y, 2)

	# # tworzenie instancji silnika
	# silnik_X = SilnikDC(KANAL_SILNIK_DC_X)
	# silnik_Y = SilnikDC(KANAL_SILNIK_DC_Y)

	while True:
		print("X: ", krancowka_X.check_state())
		print("Y: ", krancowka_Y.check_state())
		time.sleep(2)







if __name__ == '__main__':
	main()





































# channel = 12

# def main():
# 	print("Hello, world")
# 	GPIO.setmode(GPIO.BCM)
# 	# GPIO.setwarnings(False)
# 	# GPIO.setup(channel, GPIO.OUT) #, initial=GPIO.HIGH)
# 	serwo = GPIO.PWM(channel, 50)
# 	wypelnienie = 100
# 	serwo.start(wypelnienie)
#
#
# def marker_up(serwo, wypelnienie):
# 	print("Jesteśmy w funkcji marker up")
# #	GPIO.setwarnings(False)
# #	GPIO.setup(channel, GPIO.OUT)
# 	serwo.ChangeDutyCycle(wypelnienie)
#
# def setup_serwo(channel):
# 	GPIO.setmode(GPIO.BCM)
# 	GPIO.setwarnings(False)
# 	GPIO.setup(channel, GPIO.OUT) #, initial=GPIO.HIGH)
# 	serwo = GPIO.PWM(channel, 50)
# 	serwo.start(0)
# 	return serwo
#
# try:
# 	serwo = setup_serwo(channel)
#
# 	while True:
# 		wypelnienie = input("Podaj wypelenienie: ")
# 		marker_up(serwo, int(wypelnienie))
#
# except KeyboardInterrupt:
# 	print("Close")
# finally:
# 	print('Goodbye, world!')
# 	GPIO.cleanup()
