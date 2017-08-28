import os
import time
import stomp
from .message_processor import MessageProcessor


def create_queue(resources):
    if not issubclass(resources, MessageProcessor):
        raise RuntimeError("aaa")
    return Stomp(resources)


class Stomp(object):
    _connection = None

    def __init__(self, resource_class):
        self.resource_class = resource_class

    @property
    def mq_config(self):
        return {
            'host': os.environ["AMQ_ADDRESS"],
            'port': os.environ["AMQ_PORT"],
            'user': os.environ["AMQ_USER"],
            'password': os.environ["AMQ_PASSWORD"],
            'destination': os.environ["AMQ_DESTINATION"]
        }

    def connect(self):
        self._connection = \
            stomp.Connection([(self.mq_config['host'], self.mq_config['port'])])
        while not self._connection.is_connected():
            self._connection.set_listener('', Consumer(self._connection, self.resource_class))
            self._connection.start()
            self._connection.connect(self.mq_config['user'],
                                     self.mq_config['password'],
                                     wait=True)
        self._subscribe()
        time.sleep(60 * 60)
        self._connection.disconnect()

    def _subscribe(self):
        self._connection.subscribe(destination=self.mq_config['destination'],
                                   id=1,
                                   ack='auto')


class Consumer(stomp.ConnectionListener):
    def __init__(self, conn, resource_class):
        self.app = resource_class(conn)

    def on_error(self, headers, message):
        raise StompException(headers, message)

    def on_message(self, headers, message):
        self.app.process(headers, message)

    def on_disconnected(self):
        create_queue().connect()
