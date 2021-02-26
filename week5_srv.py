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
    rsp_list = [
        b'ok\npalm.cpu 10.5 1501864247\neardrum.cpu 15.3 1501864259\npalm.cpu 8.3 1501864340\neardrum.memory 200 1501861111\n\n',
        b'ok\npalm.cpu 10.5 1501864247\neardrum.cpu 15.3 1501864259\npalm.cpu 20.3 1501864259\n\n',
        b'error\nwrong command\n\n',
        b'ok\npalm.cpu 11.5 2501864247\neardrum.cpu 15.3 1501864259\n\n',
        b'ok\npalm.cpu 12.5 2501864247\neardrum.cpu 15.3 1501864259\n\n',
        b'ok\npalm.cpu 14.5\neardrum.cpu 15.3 1501864259\n\n'
    ]

    def dynamic_rsp(vl):
        for i in vl:
            yield i

    response = dynamic_rsp(rsp_list)

    with conn:
        print('Соединение установлено:', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            request = data.decode('utf-8')
            print(f'Получен запрос: {ascii(request)}')
            print(response)
            print(f'Отправлен ответ {ascii(response)}')
            conn.sendall(next(response))

