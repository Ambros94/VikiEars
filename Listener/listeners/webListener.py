import speech_recognition as sr

from snowboy import snowboydecoder


def recognize(recognize_function):
    return recognize_function()


def start_listening():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        snowboydecoder.play_audio_file(snowboydecoder.DETECT_DING)
        print("Say something!")
        audio = r.listen(source)
        # sphinxRecognizer = lambda: r.recognize_sphinx(audio)
        heard = recognize(lambda: r.recognize_google(audio))  # , recognize(sphinxRecognizer)
        print heard
        return heard
