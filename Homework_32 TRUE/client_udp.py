import socket


SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = "Привіт, сервер"
sock.sendto(message.encode(), (SERVER_HOST, SERVER_PORT))

data, addr = sock.recvfrom(1024)
print(f"Відповідь від сервера: {data.decode()}")

sock.close()
