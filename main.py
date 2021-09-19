import json
import socket


def server():
    sock = socket.socket()
    qwert = ('', 8395)
    sock.bind(qwert)
    sock.listen(1)

    conn, addr = sock.accept()  # возвращаем кортеж с двумя єлементами (новый_сокет, адрес клиента) с помощью метода accept

    while True:
        data = conn.recv(1024) # воспользуемся методом recv, который в качестве аргумента принимает количество байт для чтения. Мы будем читать порциями по 1024 байт (и
        data = data.decode()
        with open("dns_list", "r") as read_file:
            json_dns = json.load(read_file)
        if data not in json_dns["dns_list"]:
            conn.send("unknow domen".encode())
            conn.close()
            break
        ip = json_dns["dns_list"][data]
        conn.send(ip.encode())

    conn.close()


if __name__ == "__main__":
    server()
