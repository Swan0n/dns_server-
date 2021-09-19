import json
import socket


def chek_server():
    prox_sock = socket.socket()
    prox_qwert = ('', 8397)
    prox_sock.bind(prox_qwert)
    prox_sock.listen(1)

    conn, addr = prox_sock.accept()  # возвращаем кортеж с двумя єлементами (новый_сокет, адрес клиента) с помощью метода accept
    print(f"Connect: {addr}")

    while True:
        data = conn.recv(
            1024)  # воспользуемся методом recv, который в качестве аргумента принимает количество байт для чтения. Мы будем читать порциями по 1024 байт (и
        data = data.decode()
        print(data)
        if not data:
            break
        with open("black_list", "r") as read_file:
            data_bl = json.load(read_file)
        if data in data_bl["black_list"]:
            conn.send("ip is in black list".encode())
            break

        dns_sock = socket.socket()
        dns_sock.connect(('localhost', 8395))
        dns_sock.send(data.encode())

        ip = dns_sock.recv(1024)
        dns_sock.close()

        conn.send(ip)

    conn.close()


if __name__ == "__main__":
    chek_server()
