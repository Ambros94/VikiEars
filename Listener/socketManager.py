from socketIO_client import SocketIO

import TTS

socket = None


def textCommandResponse(*args):
    from listeners import magicListener
    response_status = args[0]
    print "ResponseStatus:" + response_status
    if response_status == "UNKNOWN":
        TTS.say(TTS.unknown_response)
    elif response_status == "OK":
        # Special case. All completed, W8 for next hotKey
        TTS.say(TTS.ok_response)
        magicListener.startKeyword()
        return
    elif response_status == "LOW_CONFIDENCE":
        TTS.say(TTS.confidence_response)
    elif response_status == "MISSING_NUMBER":
        TTS.say(TTS.number_response)
    elif response_status == "MISSING_LOCATION":
        TTS.say(TTS.location_response)
    elif response_status == "MISSING_COLOR":
        TTS.say(TTS.color_response)
    elif response_status == "TEACH":
        TTS.say(TTS.teach_response)
    elif response_status == "LEARNED":
        TTS.say(TTS.learned_response)
    elif response_status == "MISSING_DATETIME":
        TTS.say(TTS.dateTime_response)
    elif response_status == "MISSING_FREE_TEXT":
        TTS.say(TTS.freeTextResponse)
    else:
        TTS.error()
    # W8 for the next sentence
    magicListener.startSentence()


def init_connection():
    global socket
    socket = SocketIO('localhost', 8887)


def send(message):
    global socket
    if socket is None:
        init_connection()
    # Send the message on the socket and print the result
    socket.emit("textCommand", message, textCommandResponse)
    socket.wait_for_callbacks(seconds=30)


def close():
    global socket
    socket.disconnect()
