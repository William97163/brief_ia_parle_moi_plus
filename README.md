# Brief ia parle moi plus 

## Guide d'installation

Pour commencer à utiliser l'application vous devez commencer à utiliser l'application, vous devez d'abord : 
- Intaller le requirement.txt à l'aide de la commande suivante : 'pip install requirement.txt'
- Utiliser la commande : 'streamlit run app.py' pour lancer l'application streamlit

## Repository

Le fichier app.py contient tout le code utilisé pour l'application streamlit 

le fichier utils.py contient la fonction speech avec azure 

le fichier speech.py contient la fonction speech sans azure

## Librairie Utilisés

- streamlit
- openai
- speech_recognition
- azure.cognitiveservices.speech

## Partie 2 : Speech recognition sans Azure

Pour réaliser cette partie j'ai importé la librairie speech recognition de google pour refaire une fonction presque identique que celle d'azure (recognize_from_microphone)

Je n'ai donc pas utiliser de model personnalisé pour cette partie

