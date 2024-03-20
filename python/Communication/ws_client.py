import asyncio
import websockets

async def client():
    async with websockets.connect("ws://localhost:8080") as websocket:
        print("Connected to the WebSocket server")
        await websocket.send("Hello, server!")
        response = await websocket.recv()
        print(f"Received: {response}")

asyncio.get_event_loop().run_until_complete(client())
