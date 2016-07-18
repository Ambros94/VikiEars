# Start keyword listening
# When the keyword appears
# Stop listening
# Activate google listening

# Global variable used to interrupt the system
import signal

import sentenceSender
from listeners import magicListener

interrupted = False


def signal_handler(signal, frame):
    print "Manual shutdown requested !"  # TODO Stop the listening callback
    global interrupted
    interrupted = True
    sentenceSender.close()


# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)
# Start the listener that detects the keywords
magicListener.start()
