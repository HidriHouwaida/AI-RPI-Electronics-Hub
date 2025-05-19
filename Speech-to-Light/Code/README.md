# Explication du Code - LED Clignotante

## Fichier : `basic_blink_led.py`

### Structure du Code

```python

# Importation des bibliothèques
import RPi.GPIO as GPIO  # Pour contrôler les GPIO
import time              # Pour les pauses

#Explication de GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BCM)  # Configuration du mode de numérotation GPIO

##Fonction
Cette ligne spécifie le mode d'identification des broches GPIO sur le Raspberry Pi.

##Les deux modes disponibles
| Mode GPIO       | Type de numérotation | Exemple     | Avantages                     |
|-----------------|-----------------------|------------------|-------------------------------|
| `GPIO.BCM`      | Logique (Broadcom)    | GPIO17, GPIO18   | Compatible tous modèles RPi    |
| `GPIO.BOARD`    | Physique (broches)    | Broche 11 = GPIO17 | Visuel facile (câblage)       |
