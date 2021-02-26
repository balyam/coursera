import socket
import time


class Client:
    def __init__(self, conn, port, timeout=None):
        self.sock = socket.create_connection((conn, port), timeout)

    def get(self, metric):
        msg = f"get {metric}\n"
        self.sock.sendall(msg.encode('utf-8'))
        response = self.sock.recv(1024).decode('utf-8')
        arr = response.split("\n")
        if arr[0] == 'ok':
            del arr[0]
            del arr[-2:]
            print(arr)
            return self.reformat(arr)
        raise ClientError

    def put(self, metric, metric_value, timestamp=None):
        if timestamp is None:
            timestamp = int(time.time())
        msg = f"put {metric} {metric_value} {timestamp}\n"
        self.sock.sendall(msg.encode('utf-8'))
        response = self.sock.recv(1024).decode('utf-8')
        arr = response.split("\n")
        if arr[0] == 'error':
            raise ClientError

    def close(self):
        self.sock.close()

    @staticmethod
    def reformat(data: list) -> dict:
        recieved_data = {}
        for elt in data:
            try:
                rsp_str = elt.split(' ')
                if rsp_str[0] in recieved_data:
                    recieved_data[rsp_str[0]].append((int(rsp_str[2]), float(rsp_str[1])))
                else:
                    recieved_data[rsp_str[0]] = [(int(rsp_str[2]), float(rsp_str[1]))]
            except (IndexError, ValueError):
                raise ClientError
        for key, value in recieved_data.items():
            value.sort(key=lambda tup: tup[0])
        return recieved_data


class ClientError(socket.error):
    def __str__(self):
        return f"<ClientException> message"
