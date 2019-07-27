#!/usr/bin/python3

#Name: Lisa van Dyk
#Student Number: VDYLIS001
#Practical 1
#27 July 2019

#import relevant libraries
import RPi.GPIO as GPIO
import time as time

def main():
	time.sleep(0.5)
	GPIO.output(3,GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(3,GPIO.LOW)

def setup():
	GPIO.setmode(GPIO.BOARD)					#Set pin numbering system
	GPIO.setup(3,GPIO.OUT, initial=GPIO.LOW)

#only run function if
if __name__ == "__main__":
	try:
		while True:
			setup()
			main()
	except KeyboardInterrupt:
		print("Exiting gracefully")
		GPIO.cleanup()						#Turn off GPIOs
	except:
		print("Some other error occurred")
