# реализация сервера для тестирования метода get по заданию - Клиент для отправки метрик
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
with socket.socket() as sock:
    sock.bind(('127.0.0.1', 10001))
    sock.listen(5)
    conn, addr = sock.accept()

    # переменная response хранит строку возвращаемую сервером, если вам для
    # тестирования клиента необходим другой ответ, измените ее
    response = b'ok\npalm.cpu 10.5 1501864247\neardrum.cpu 15.3 1501864259\n\n'

    with conn:
        print('Соединение установлено:', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            request = data.decode('utf-8')
            print(f'Получен запрос: {ascii(request)}')
            print(f'Отправлен ответ {ascii(response.decode("utf-8"))}')
            conn.sendall(response)

