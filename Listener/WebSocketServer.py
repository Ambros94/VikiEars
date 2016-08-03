import tornado.web as tw

import tornado.httpserver as th
import tornado.websocket as tws
import tornado.ioloop
import socketManager as so

class MyWebSocketServer(tws.WebSocketHandler):
    def open(self):
        # metodo eseguito all'apertura della connessione
        print 'Nuova connessione'

    def on_message(self, message):
        # metodo eseguito alla ricezione di un messaggio
        # la stringa 'message' rappresenta il messaggio
        print 'Messaggio ricevuto: %s' % message

    def on_close(self):
        # metodo eseguito alla chiusura della connessione
        print 'Connessione chiusa'

    def check_origin(self, origin):
        return True


application = tw.Application([
    (r'/websocketserver', MyWebSocketServer),
])

http_server = tornado.httpserver.HTTPServer(application)
http_server.listen(8888)

tornado.ioloop.IOLoop.instance().start()
