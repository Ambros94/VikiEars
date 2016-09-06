import speech_recognition as sr

import socketManager
import webListener
from snowboy import snowboydecoder

interrupted = False


def request_shutdown():
    global interrupted
    interrupted = True


def activation_detected(detector):
    # Notify that the how keyword has been detected
    print "Speak now!"
    # Shut down the keywords lister
    detector.terminate()
    # Start sentenceListener
    startSentence()


def startSentence():
    try:
        heard = webListener.start_listening()
        socketManager.send(heard)
    except sr.UnknownValueError:
        snowboydecoder.play_audio_file(snowboydecoder.DETECT_DONG)
        startKeyword()
        print("Speech Recognition could not understand audio")
    except sr.RequestError as e:
        snowboydecoder.play_audio_file(snowboydecoder.DETECT_DONG)
        print("Could not request results from Speech Recognition service; {0}".format(e))


def interrupt_callback():
    global interrupted
    return interrupted


def startKeyword():
    # Configure keyword listener
    models = ["resources/jarvis.pmdl"]
    sensitivity = [0.45] * len(models)
    detector = snowboydecoder.HotwordDetector(models, sensitivity=sensitivity)
    callbacks = [lambda: activation_detected(detector)]
    # Start keyword listener
    print "Waiting for the keyword !"
    detector.start(detected_callback=callbacks,
                   interrupt_check=interrupt_callback,
                   sleep_time=0.03)
