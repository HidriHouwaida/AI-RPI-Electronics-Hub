# Explication du Code 

## Fichier : `basic_blink_led.py`

### Structure du Code

```python

# Importation des bibliothèques
import RPi.GPIO as GPIO  # Pour contrôler les GPIO
import time              # Pour les pauses
```
#### Explication de GPIO.setmode(GPIO.BCM)
```python
GPIO.setmode(GPIO.BCM)  # Configuration du mode de numérotation GPIO
```
##### Fonction
Cette ligne spécifie le mode d'identification des broches GPIO sur le Raspberry Pi.

##### Les deux modes disponibles
| Mode GPIO       | Type de numérotation | Exemple            | Avantages                     |
|-----------------|----------------------|--------------------|-------------------------------|
| `GPIO.BCM`      | Logique (Broadcom)   | GPIO17, GPIO18     |  Compatible tous modèles RPi  |
| `GPIO.BOARD`    | Physique (broches)   | Broche 11 = GPIO17 | Visuel facile (câblage)       |
```python
LED_PIN = 17  # Définit le numéro de broche GPIO en mode BCM (logique)
GPIO.setup(LED_PIN,GPIO.OUT) # Configure la broche GPIO17 en mode sortie
```
#### Boucle de Clignotement Infini
```python
while True:
    GPIO.output(LED_PIN, GPIO.HIGH)  # Allume la LED
    time.sleep(1)                   # Pause de 1 seconde
    GPIO.output(LED_PIN, GPIO.LOW)   # Éteint la LED
    time.sleep(1)                   # Pause de 1 seconde
```
##### Fonctionnement Pas-à-Pas
| Ligne de Code                  | Action	                                                        |Durée       |
|--------------------------------|------------------------------------------------------------------|------------|
| GPIO.output(LED_PIN, GPIO.HIGH)| Envoie un signal 3.3V (niveau logique HIGH) à la broche GPIO17	| Instantané |
| time.sleep(1)	Maintient la LED | allumée pendant 1 seconde	                                    | 1 seconde  |
| GPIO.output(LED_PIN, GPIO.LOW) | Coupe le signal (0V / niveau logique LOW)	                    | Instantané |
| time.sleep(1)	                 | Maintient la LED éteinte pendant 1 seconde	                    |  1 seconde |
## Fichier : `SpeechToLight.py`

### Structure du Code

```python

# Importation des bibliothèques
import speech_recognition as sr  # pour la conversion de la parole (voix) en texte
import RPi.GPIO as GPIO          # Pour contrôler les GPIO
from googletrans import Translator # pour la traduction automatique de texte
import time                      # pour les pauses
```
#### Explication de la fonction translate_to_anglais(text)

```python

def translate_to_anglais(text):
    """Traduit le texte en anglais """
    try:
        translated = translator.translate(text, dest='en')  
        return translated.text.lower()                     
    except Exception as e:
        print(f"Erreur de traduction: {e}")
        return text.lower()                                

```

##### Rôle 
Traduit un texte depuis n'importe quelle langue vers l'anglais et retourne le résultat en minuscules.

##### Fonctionnement 

* Utilise le service Google Translate via la bibliothèque googletrans  
* Prend en entrée un texte (`text`) dans n'importe quelle langue  
* Tente de le traduire en anglais (`dest='en'`)  
**En cas de succès** 
  *Retourne la traduction en minuscules 
**En cas d'échec  ** 
  *Affiche l'erreur dans la console
  *Retourne le texte original en minuscules
  
#### Explication de la fonction process_command(command_en)

```python

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

```
##### Rôle
Cette fonction contrôle le LED en fonction de la  commande vocale traduite en anglais.

##### Fonctionnement

 * Elle reçoit la commande en anglais (command_en) 

 * Elle vérifie d'abord si la commande existe (n'est pas vide)

 * Elle compare la commande avec deux actions possibles :

   * Si la commande contient "light up" → allume la LED (GPIO.HIGH)

   * Si la commande contient "light off" → éteint la LED (GPIO.LOW)

 * Retourne True si la commande a été reconnue et exécutée, False sinon

#### Explication de la fonction listen_and_translate()

```python

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

```

##### Rôle
Cette fonction capture la commande vocale via le microphone, la reconnaît et la traduit en anglais.

##### Fonctionnement

 * Initialisation :

   * Ouvre le microphone comme source audio

   * Affiche une invite pour l'utilisateur

 * Traitement audio :

   * Ajuste le niveau du bruit ambiant

   * Écoute l'entrée microphone avec un timeout de 5 secondes

 * Reconnaissance vocale :

   * Utilise l'API Google Speech Recognition

   * Accepte toutes les langues (language=None)

   * Affiche le texte reconnu

 * Traduction :

   * Envoie le texte à la fonction translate_to_anglais()

   * Retourne le résultat traduit
 * Gestion d'erreurs :

   * Commande incomprise → Message "Je n'ai pas compris"

   * Erreur API → Affiche le détail technique

   * Erreur générale → Message d'erreur inattendue
