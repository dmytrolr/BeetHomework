import socket

def caesar_cipher(text, shift):
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return "".join(result)

HOST = "127.0.0.1"
PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

print(f"UDP-сервер із шифром Цезаря запущено {HOST}:{PORT}")

client_keys = {}

while True:
    data, addr = sock.recvfrom(1024)
    message = data.decode()

    if addr not in client_keys:
        try:
            client_keys[addr] = int(message)
            sock.sendto(f"Ключ {message} збережено".encode(), addr)
        except ValueError:
            sock.sendto(b"ERROR: KEY MUST BE A DIGIT ONLY", addr)
    else:
        shift = client_keys[addr]
        encrypted = caesar_cipher(message, shift)
        sock.sendto(encrypted.encode(), addr)
