import speech_recognition as sr

import sentenceSender
import webListener
from snowboy import snowboydecoder


def ehi_vicky(detector):
    # Notify that the how keyword has been detected
    print "Said : Hei vicky"
    snowboydecoder.play_audio_file(snowboydecoder.DETECT_DING)
    # Shut down the keywords lister
    detector.terminate()
    # Start sentenceListener
    try:
        heard = webListener.start_listening()
        sentenceSender.send(heard)
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
    return False  # TODO This is not the proper way.. Ask someone that knows python


def start():
    # Configure keyword listener
    models = ["resources/vicky.pmdl", "resources/cancel.pmdl"]
    sensitivity = [0.5] * len(models)
    detector = snowboydecoder.HotwordDetector(models, sensitivity=sensitivity)
    callbacks = [lambda: ehi_vicky(detector),
                 cancel]
    # Start keyword listener
    print "Waiting for the keyword !"
    detector.start(detected_callback=callbacks,
                   interrupt_check=interrupt_callback,
                   sleep_time=0.03)
