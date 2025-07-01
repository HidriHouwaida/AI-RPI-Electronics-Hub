import speech_recognition as sr 
import RPi.GPIO as GPIO 
import time 

GPIO.setmode(GPIO.BCM)
LED_PIN=17
GPIO.setup(LED_PIN,GPIO.OUT)


