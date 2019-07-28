#!/usr/bin/python3

#Name: Lisa van Dyk
#Student Number: VDYLIS001
#Practical 1
#27 July 2019

#import relevant libraries
import RPi.GPIO as GPIO
import time as time

#Global variables
switch_list = [11,13]							#Array of pins connected to the switches
LED_list = [3,5,7]							#Array of pins connected to LEDS
counter=0								#Variable that keeps track of what number is to be displayed
direction=1								#Variable that keeps track of direction of counting

def main():
	global direction
	global counter

	LED(counter)
	time.sleep(1)
	if GPIO.event_detected(11):					#When Switch 1 is pressed - count forwards
		direction =1

	if GPIO.event_detected(13):					#When Switch 2 is pressed - count backwards
		direction = 0

	count(direction)

def count(c):								#Function that increments/decrements counter
	global counter
	if (c==1):
		if (counter == 7):
			counter=0					#Counter loops back  from 7 to zero
		else:
			counter+=1					#Counter increments

	if (c==0):
		if (counter == 0):
			counter=7					#Counter loops from 7  to zero
		else:
			counter-=1					#Counter decrements

def LED(c):								#Function that will realize binary number on LED's
	if (c==0):
		GPIO.output(LED_list,0)

	if (c==1):
		GPIO.output(LED_list, (0,0,1))

	if (c==2):
		GPIO.output(LED_list, (0,1,0))

	if (c==3):
		GPIO.output(LED_list, (0,1,1))

	if (c==4):
		GPIO.output(LED_list, (1,0,0))

	if (c==5):
		GPIO.output(LED_list, (1,0,1))

	if (c==6):
		GPIO.output(LED_list, (1,1,0))

	if (c==7):
		GPIO.output(LED_list, (1,1,1))

def setupLED():
	global LED_list
	GPIO.setmode(GPIO.BOARD)					#Set pin numbering system
	GPIO.setwarnings(False)
	GPIO.setup(LED_list, GPIO.OUT, initial=GPIO.LOW)

def setupSWITCH():
	global switch_list
	GPIO.setup(switch_list,GPIO.IN,pull_up_down=GPIO.PUD_UP)	#Set pin 13 and 15 as input pins

#only run function if
if __name__ == "__main__":
	try:
		setupLED()
		setupSWITCH()
		GPIO.add_event_detect(11, GPIO.RISING, bouncetime=200)			#Add interrupts to pins connected to switches
		GPIO.add_event_detect(13, GPIO.RISING, bouncetime=200)

		while True:
			main()

	except KeyboardInterrupt:
		print("Exiting gracefully")
		GPIO.cleanup()						#Turn off GPIOs
	except:
		GPIO.cleanup()
		print("Some other error occurred")
		print(e.message)

