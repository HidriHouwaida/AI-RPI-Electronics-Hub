import speech_recognition as sr 
import RPi.GPIO as GPIO 
import time 

GPIO.setmode(GPIO.BCM)
LED_PIN=17
GPIO.setup(LED_PIN,GPIO.OUT)

r=sr.Recognizer()
with sr.Microphone() as source : 
  print("Say Something ")
  audio=r.listen(source)
  voice_data=r.recognize_google(audio) 
