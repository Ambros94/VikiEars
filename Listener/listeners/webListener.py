import speech_recognition as sr


def recognize(recognize_function):
    return recognize_function()


def start_listening():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        # recognize speech using Google Speech Recognition
        # heard = r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")
        # sphinxRecognizer = lambda: r.recognize_sphinx(audio)

        heard = recognize(lambda: r.recognize_google(audio))  # , recognize(sphinxRecognizer)
        print heard
        print("Google Speech Recognition thinks you said: " + heard)
        return heard
