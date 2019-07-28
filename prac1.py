#!/usr/bin/python3

#Name: Lisa van Dyk
#Student Number: VDYLIS001
#Practical 1
#27 July 2019

#import relevant libraries
import RPi.GPIO as GPIO
import time as time

switch_list = [11,13]

def main():
	if GPIO.event_detected(11):
		GPIO.output(3,GPIO.HIGH)

	if GPIO.event_detected(13):
		GPIO.output(3,GPIO.LOW)

def setupLED():
	GPIO.setmode(GPIO.BOARD)					#Set pin numbering system
	GPIO.setwarnings(False)
	GPIO.setup(3,GPIO.OUT, initial=GPIO.LOW)

def setupSWITCH():
	global switch_list
	GPIO.setup(switch_list,GPIO.IN,pull_up_down=GPIO.PUD_UP)	#Set pin 13 and 15 as input pins
 
#only run function if
if __name__ == "__main__":
	try:
		setupLED()
		setupSWITCH()
		GPIO.add_event_detect(11, GPIO.RISING)			#Add interrupts to pins connected to switches
		GPIO.add_event_detect(13, GPIO.RISING)

		while True:
			main()

	except KeyboardInterrupt:
		print("Exiting gracefully")
		GPIO.cleanup()						#Turn off GPIOs
	except:
		print("Some other error occurred")
		print(e.message)

