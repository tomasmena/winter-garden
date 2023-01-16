import socket
import websockets
import asyncio


PORT = 7890
url="127.0.0.1"
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(("url",1026))
# s.listen(5)

# while True:
#     clientsocket,address=s.accept()
#     print(f"Connection from {address} has been established!")
#     clientsocket.send(bytes("Welcome to the server","utf-8"))
#     clientsocket.close()

# print ("Listening on PORT "+ str(PORT))

async def echo(websocket,path):
    print("someone connected")
    async for message in websocket:
        print("received "+ message) 
        await websocket.send(message + "received")

start_server=websockets.serve(echo,url,PORT)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()


# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(("0.0.0.0",1026))
# s.listen(5)

# while True:
#     clientsocket,address=s.accept()
#     print(f"Connection from {address} has been established!")
#     clientsocket.send(bytes("Welcome to the server","utf-8"))
#     clientsocket.close()






# ###------------- Clietn ------------------
# async def listen():
#     url="http://192.168.178.32/"

#     async with websockets.connect(url) as ws:
#         while True:
#             msg = await ws.recv()
#             print(msg)

# asyncio.get_event_loop().run_until_complete(listen())
