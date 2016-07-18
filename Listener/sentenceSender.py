from socketIO_client import SocketIO

socket = None


def ack_received():
    print "ack received"


def connect():
    print "connect"


def reconnect():
    print "reconnect"


def init_connection():
    global socket
    socket = SocketIO('localhost', 8887)
    socket.on('ack', ack_received)
    socket.on('connect', connect)
    socket.on('reconnect', reconnect)


def send(message):
    if socket is None:
        init_connection()
    print message + "<- this is the message"
    # Send the message on the socket and print the result
    socket.emit("command", message)


def close():
    socket.close()
