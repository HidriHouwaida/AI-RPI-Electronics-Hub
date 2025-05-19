# Explication du Code - LED Clignotante

## Fichier : `basic_blink_led.py`

### Structure du Code

```python

# Importation des bibliothèques
import RPi.GPIO as GPIO  # Pour contrôler les GPIO
import time              # Pour les pauses
'''
#Explication de GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BCM)  # Configuration du mode de numérotation GPIO

##Fonction
Cette ligne spécifie le mode d'identification des broches GPIO sur le Raspberry Pi.

##Les deux modes disponibles
| Mode GPIO       | Type de numérotation | Exemple            | Avantages                     |
|-----------------|----------------------|--------------------|-------------------------------|
| `GPIO.BCM`      | Logique (Broadcom)   | GPIO17, GPIO18     |  Compatible tous modèles RPi  |
| `GPIO.BOARD`    | Physique (broches)   | Broche 11 = GPIO17 | Visuel facile (câblage)       |
|---------------------------------------------------------------------------------------------|

LED_PIN = 17  # Définit le numéro de broche GPIO en mode BCM (logique)
GPIO.setup(LED_PIN,GPIO.OUT) # Configure la broche GPIO17 en mode sortie
#Boucle de Clignotement Infini

while True:
    GPIO.output(LED_PIN, GPIO.HIGH)  # Allume la LED
    time.sleep(1)                   # Pause de 1 seconde
    GPIO.output(LED_PIN, GPIO.LOW)   # Éteint la LED
    time.sleep(1)                   # Pause de 1 seconde
#Fonctionnement Pas-à-Pas
Fonctionnement Pas-à-Pas
| Ligne de Code                  | Action	                                                        |Durée       |
|--------------------------------|----------------------------------------------------------------|------------|
| GPIO.output(LED_PIN, GPIO.HIGH)| Envoie un signal 3.3V (niveau logique HIGH) à la broche GPIO17	| Instantané |
| time.sleep(1)	Maintient la LED | allumée pendant 1 seconde	                                    | 1 seconde  |
| GPIO.output(LED_PIN, GPIO.LOW) | Coupe le signal (0V / niveau logique LOW)	                    | Instantané |
| time.sleep(1)	                 | Maintient la LED éteinte pendant 1 seconde	                    |  1 seconde |
|--------------------------------|----------------------------------------------------------------|------------|
