import asyncio

async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    addr = writer.get_extra_info('peername')
    print(f"[+] Нове з'єднання від {addr}")

    try:
        while True:
            data = await reader.read(1024)
            if not data:
                break
            message = data.decode()
            print(f"[{addr}] {message.strip()}")
            writer.write(data)
            await writer.drain()
    except asyncio.CancelledError:
        pass
    finally:
        print(f"[-] З'єднання закрито {addr}")
        writer.close()
        await writer.wait_closed()

async def main():
    server = await asyncio.start_server(handle_client, '127.0.0.1', 8888)
    addr = server.sockets[0].getsockname()
    print(f"[~] Echo-сервер запущено на {addr}")

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
