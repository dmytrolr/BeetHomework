import socket


HOST = "127.0.0.1"
PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

print(f"UDP-server running {HOST}:{PORT}")

while True:
    data, addr = sock.recvfrom(1024)
    print(f"Отримано від {addr}: {data.decode()}")
    sock.sendto(b"Message recived", addr)
