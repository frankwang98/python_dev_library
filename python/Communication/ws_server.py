import asyncio
import websockets
import signal

async def server(websocket, path):
    print("A new client connected")
    try:
        while True:
            message = await websocket.recv()
            print(f"Received: {message}")
            await websocket.send("Hello, client!")
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")

start_server = websockets.serve(server, "localhost", 8080)

# 是一个关不掉的窗口
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
