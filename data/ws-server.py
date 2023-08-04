import asyncio
import websockets

async def server(websocket, path):
    async for message in websocket:
        # Handle incoming message
        print(f"Received message: {message}")
        
        # Send response
        response = f"Received message: {message}"
        await websocket.send(response)

async def main():
    async with websockets.serve(server, "localhost", 8765):
        await asyncio.Future()  # Run forever

asyncio.run(main())