import os
import socket
import time


class Client:
    def __init__(self, conn, port, timeout=None):
        with socket.create_connection((conn, port), timeout) as sock:
            self.sock = sock
            self.sock.settimeout(0)

    def get(self, metric):
        msg = metric.encode()
        self.sock.sendall(msg)
        recieved_data = []
        while True:
            response = self.sock.recv(1024)
            if not response:
                print(recieved_data)
                break
            else:
                recieved_data.append(response.decode('utf-8'))

    def put(self, metric, metric_value, timestamp=int(time.time())):
        raise ClientException


class ClientException(socket.error):
    def __str__(self):
        return f"<ClientException> message"
