import socket
import multiprocessing

HOST = "127.0.0.1"
PORT = 5000

def handle_client(conn, addr):
    print(f"[+] Нове з'єднання від {addr}")
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"[{addr}] {data.decode('utf-8')}")
            conn.sendall(data)
    print(f"[-] З'єднання закрито {addr}")

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()
        print(f"Сервер запущено на {HOST}:{PORT}")

        while True:
            conn, addr = server.accept()
            process = multiprocessing.Process(target=handle_client, args=(conn, addr))
            process.daemon = True  # процес завершиться разом із сервером
            process.start()
            print(f"[INFO] Активних процесів: {len(multiprocessing.active_children())}")

if __name__ == "__main__":
    main()
