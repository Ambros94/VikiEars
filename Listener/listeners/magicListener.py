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
    try:
        heard = webListener.start_listening()
        socketManager.send(heard)
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Speech Recognition service; {0}".format(e))
    # Restart keyword listener
    start()


def cancel():
    print "Said : Vicky delete"
    snowboydecoder.play_audio_file(snowboydecoder.DETECT_DONG)


def interrupt_callback():
    global interrupted
    return interrupted


def start():
    # Configure keyword listener
    models = ["resources/jarvis.pmdl", "resources/cancel.pmdl"]
    sensitivity = [0.45] * len(models)
    detector = snowboydecoder.HotwordDetector(models, sensitivity=sensitivity)
    callbacks = [lambda: activation_detected(detector),
                 cancel]
    # Start keyword listener
    print "Waiting for the keyword !"
    detector.start(detected_callback=callbacks,
                   interrupt_check=interrupt_callback,
                   sleep_time=0.03)
