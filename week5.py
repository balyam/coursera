import socket
import time


class Client:
    def __init__(self, conn, port, timeout=None):
        self.sock = socket.create_connection((conn, port), timeout)
        # with socket.create_connection((conn, port), timeout) as sock:
        #     self.sock = sock
        # self.sock.settimeout(0)

    def get(self, metric):
        msg = f"get {metric}\n"
        self.sock.sendall(msg.encode('utf-8'))
        recieved_data = {}
        response = self.sock.recv(1024).decode('utf-8')
        arr = response.split("\n")
        if arr[0] == 'ok':
            del arr[0]
            # arr.remove('')
            print(arr)

            for elt in response:
                tmp_arr = elt.split()
                recieved_data[tmp_arr[0]] = (tmp_arr[2], tmp_arr[1])
        return recieved_data

    def put(self, metric, metric_value, timestamp=int(time.time())):
        raise ClientException

    def close(self):
        self.sock.close()


class ClientException(socket.error):
    def __str__(self):
        return f"<ClientException> message"
