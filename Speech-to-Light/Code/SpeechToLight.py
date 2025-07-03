import speech_recognition as sr
import RPi.GPIO as GPIO
from googletrans import Translator
import time

# Configuration GPIO
LED_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# Initialisation des services
recognizer = sr.Recognizer() # création d'un objet de la classe Recognizer en utilisant un constructeur vide
translator = Translator()    # création d'un objet de la classe Translator en utilisant un constructeur vide 

def translate_to_anglais(text):
    """Traduit le texte en anglais """
    try:
        translated = translator.translate(text, dest='en') # utilisation de la fonction transalte de la classe Tranlator pour la traduction de texte vers l'anglais 
        return translated.text.lower()                     # pour retourner le texte traduite en miniscules 
    except Exception as e:
        print(f"Erreur de traduction: {e}")
        return text.lower()                                # pour retourner le texte initiale en miniscules 

def process_command(command_en):
    """Traite la commande traduite en anglais"""
    if not command_en:
        return False
    
    print(f"Commande traduite: {command_en}")
    
    if "light up" in command_en :
        GPIO.output(LED_PIN, GPIO.HIGH)
        print("Led On ")
        return True
    elif "light off" in command_en :
        GPIO.output(LED_PIN, GPIO.LOW)
        print("LED Off")
        return True
    
    return False

def listen_and_translate():
    """Ecoute, reconnait et traduit la commande vocale"""
    with sr.Microphone() as source:
        print("Dites 'allumer' ou 'eteindre' dans votre langue...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5)
        
        try:
            text = recognizer.recognize_google(audio, language=None)
            print(f"Vous avez dit: {text}")
            return translate_to_french(text)
            
        except sr.UnknownValueError:
            print("Je n'ai pas compris l'audio")
        except sr.RequestError as e:
            print(f"Erreur du service de reconnaissance; {e}")
        except Exception as e:
            print(f"Erreur inattendue: {e}")
        
        return None

# Boucle principale
try:
    while True:
        french_command = listen_and_translate()
        if not process_command(french_command):
            print("Commande non reconnue. Essayez avec 'allumer' ou 'eteindre'")
        time.sleep(1)

except KeyboardInterrupt:
    print("Arret du programme")
finally:
    GPIO.cleanup()
