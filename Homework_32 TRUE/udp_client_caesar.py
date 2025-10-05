import socket

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

key = 4
sock.sendto(str(key).encode(), (SERVER_HOST, SERVER_PORT))
data, _ = sock.recvfrom(1024)
print("Сервер:", data.decode())

message = "Привіт, сервер"
sock.sendto(message.encode(), (SERVER_HOST, SERVER_PORT))
data, _ = sock.recvfrom(1024)
print("Зашифрована відповідь:", data.decode())

sock.close()
