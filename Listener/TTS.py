import random
from os import system

unknown_response = ["I do not know what u said"]
ok_response = ["Done.", "Ok.", "Perfect.", "As you said.", "Yes Sir.", "As you wish"]
confidence_response = ["Rephrase it", "I am not so sure about what you said"]
number_response = ["Missing a value", "Number missing"]
location_response = ["Where?", "Missing location"]
color_response = ["You must give me the color", "A color is missing"]
dateTime_response = ["When ?", "Missing date", "Missing time"]
freeTextResponse = ["Do What ?", "I miss your argument"]


def say(sentence_array):
    _say(random.choice(sentence_array))


def _say(message):
    system('say ' + message)


def error():
    _say("UNKNOWN STATUS CODE")
