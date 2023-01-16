import socket
import websockets
import asyncio
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect(("127.0.0.1",1026))
# complete_info=""
# while True:
#     msg=s.recv(8)
#     if len(msg)==0:
#         break
#     complete_info+=msg.decode("utf-8")

# print(complete_info)


async def listen():
    url="wss://winter-garden-server.glitch.me"

    async with websockets.connect(url) as ws:
        while True:
            msg = await ws.recv()
            print(msg)

asyncio.get_running_loop().run_until_complete(listen())


