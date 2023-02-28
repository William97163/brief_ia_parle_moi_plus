import os
import azure.cognitiveservices.speech as speechsdk
import openai

# Configure l'API OpenAI avec votre clé d'API
openai.api_key = os.environ.get('OPENAI_KEY')

# Configure le service Cognitive Services Speech avec vos informations d'identification
speech_config = speechsdk.SpeechConfig(
    speech_recognition_language="fr-FR",
    subscription= os.environ.get('SPEECH_KEY'),
    region= os.environ.get('SPEECH_REGION')
)

def recognize_from_microphone():
    """
    Fonction qui transcrit la parole en texte à partir d'un microphone
    """
    # Configure le microphone comme source audio
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_config.speech_recognition_language="fr-FR"
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    
    word_list = ['Sophana', 'C#', 'Scikit-learn', 'scipy', 'R', 'serverless', 'pytorch', 'seaborn', 'simplonien', 'simplonienne','Sirine','Lakhbir','Simplonline']
    
    phrase_list_grammar = speechsdk.PhraseListGrammar.from_recognizer(speech_recognizer)
    for word in word_list:       
        phrase_list_grammar.addPhrase(word)

    # Transcrit la parole en texte
    print("Parlez dans votre microphone.")
    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("text reconnu : ", speech_recognition_result.text)
        speech_config.speech_synthesis_voice_name='fr-FR-DeniseNeural'
        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
        return speech_recognition_result.text, speech_synthesizer
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print("Aucune parole n'a été reconnue : {}".format(speech_recognition_result.no_match_details))
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        print("Reconnaissance vocale annulée : {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Détails de l'erreur : {}".format(cancellation_details.error_details))
            print("Avez-vous configuré la clé de ressource de parole et les valeurs de région ?")
    return ""

def generate_response(prompt, tchat_list):
    """
    Fonction qui génère une réponse à partir d'une requête
    """
    
    mode_tchat = f"Si j étais dans la conversation suivante : '{tchat_list}' et qu une personne rajoutais cela {prompt} je lui dirai :"
    mode_compliment = f'Si je devait faire un compliment à une personne du nom de {prompt}, je dirais :'
    
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=mode_tchat,
        temperature=0.7,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    tchat_list.append(response.choices[0].text.strip())
    
    return response.choices[0].text.strip()

# # # Boucle principale du programme
# while True:
#     # Transcrit la parole en texte
#     speech_text = recognize_from_microphone()
#     if not speech_text:
#         continue

#     # Génère une réponse à partir du texte transcrit
#     response = generate_response(speech_text)

#     # Affiche la réponse
#     print(response)

#     # Synthétise la réponse vocalement
#     speech_synthesizer.speak_text_async(response).get()
