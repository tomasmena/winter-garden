import socket
import websockets
import asyncio
import socket
import streamlit as st
#url="ws://127.0.0.1:7890"
url="ws://winter-garden-server.glitch.me"
#s = socket.socket(socket.AF_LINK,socket.SOCK_STREAM)#
# s.connect("ws://winter-garden-server.glitch.me")
# complete_info=""
# while True:
#     msg=s.recv(8)
#     if len(msg)==0:
#         break
#     complete_info+=msg.decode("utf-8")

# print(complete_info)

async def listen():
    # url="ws://winter-garden-server.glitch.me"
        async with websockets.connect(url) as websocket:
            await websocket.send("hello server")
            while True:
                msg = await websocket.recv()
                print((msg))
                return msg

#asyncio.get_event_loop().run_until_complete(listen())
# deque 