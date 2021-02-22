import os
import socket
from time import time





class Client:
    def __init__(self, conn, port, timeout=None):
        self.conn = conn
        self.port = port
        self.timeout = timeout
        socket.create_connection((self.conn, self.port), self.timeout)

    def get(self, metric_value):
        raise ClientException

    def put(self, metric, metric_value, timestamp=int(time.time())):
        raise ClientException


class ClientException(Exception):
    pass
