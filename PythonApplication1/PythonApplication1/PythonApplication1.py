import speech_recognition as sr
recognizer_instance=sr.Recognizer
with sr.Microphone() as source:
    recognizer_instance.adjust_for_ambient_noise(source)
    print("sono in ascolto")
    audio=recognizer_instance.listen(source)
    text=recognizer_instance.recognize_google(audio, language="it-IT")
    print("google hai capito:",text)



