import speech_recognition as sr
import openai
    
def recognize():
    r = sr.Recognizer()
    print("Parlez dans votre microphone.")
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language='fr-FR', with_confidence=False)
    except sr.UnknownValueError:
        text = "Désolé, je n'ai pas compris"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=text,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )
    response_set = set(response.choices[0].text.split('\n'))
    response_text = '\n'.join(response_set)
    return text, response_text