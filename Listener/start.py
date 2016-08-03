# Start keyword listening
# When the keyword appears
# Stop listening
# Activate google listening

# Global variable used to interrupt the system
import signal

from listeners import magicListener


def signal_handler(signal, frame):
    print "Manual shutdown requested !"
    magicListener.request_shutdown()


# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)
# Start the listener that detects the keywords
magicListener.startKeyword()
