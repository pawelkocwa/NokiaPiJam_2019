import RPi.GPIO as GPIO
import time

from krancowka import Krancowka
from serwo import Serwo
from silnik_DC import SilnikDC

import calculator as calc

KANAL_KRANCOWKA_X = 16	# wyzej os x
KANAL_KRANCOWKA_Y = 20 	# nizej os y

DIR_SILNIK_DC_X = 5	# X dla DIR
DIR_SILNIK_DC_Y = 23	# Y dla DIR

STEP_SILNIK_DC_X = 6
STEP_SILNIK_DC_Y = 24

KANAL_SERWO = 12

HOME_ANGLE_X = 45
HOME_ANGLE_Y = 135




def main():
	# stworzenie instancji Serwa
	serwo = Serwo(KANAL_SERWO)

	# tworzenie isntancji krańcówek:
	krancowka_X = Krancowka(KANAL_KRANCOWKA_X, 1)
	krancowka_Y = Krancowka(KANAL_KRANCOWKA_Y, 2)

	# # tworzenie instancji silnika
	silnik_X = SilnikDC(DIR_SILNIK_DC_X, STEP_SILNIK_DC_X, 1)
	silnik_Y = SilnikDC(DIR_SILNIK_DC_Y, STEP_SILNIK_DC_Y, 2)


	silnik_X.hope(HOME_ANGLE_X)
	silnik_Y.hope(HOME_ANGLE_Y)

	serwo.serwo_down()

	while True:
		# print("X: ", krancowka_X.check_state())
		# print("Y: ", krancowka_Y.check_state())
		# time.sleep(2)
		# print("STOP X: ", krancowka_X.STOP())
		# print("STOP Y: ", krancowka_Y.STOP())

		# up_down = int(input("Czy chcesz podnieść czy opuścić (1/0) serwo: "))
        #
		# if up_down == 1:
		# 	serwo.serwo_up()
		# elif up_down == 0:
		# 	serwo.serwo_down()
		# else:
		# 	print("wpisałeś złą wartość")



		# Jeżeli krańcówka X da STOP, zatrzymaj silnik X
		if krancowka_X.STOP():
			silnik_X.STOP()
		if krancowka_Y.STOP():
			silnik_Y.STOP()



		# podaj x i y:
		# x = input("Podaj X: ")
		# y = input("Podaj Y: ")


		# alfa_X, alfa_Y = calc.convertXY(x, y)


		if(silnik_X.STOP_var == True and silnik_Y.STOP_var == True):
			break
		elif silnik_Y.STOP_var==True and silnik_X.STOP_var==False:
			silnik_X.one_step()
		elif silnik_Y.STOP_var==False and silnik_X.STOP_var==True:
			silnik_Y.one_step()
		elif silnik_Y.STOP_var==False and silnik_X.STOP_var==False:
			silnik_Y.one_step()
			silnik_X.one_step()


		time.sleep(0.001)
		print(silnik_X.__str__())
		print(silnik_Y.__str__())





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
