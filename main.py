import asyncio
import json

from typing import List

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from templates import html, pong


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="chat")
app.mount("/static", StaticFiles(directory="static"), name="pong")


CACHE = {
    "pad1": {"left": 399, "top": 158}
}
ALL_SYS = {

}


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.get("/pong")
async def get():
    return HTMLResponse(pong)


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You wrote: {data}", websocket)
            await manager.broadcast(f"Client #{client_id} says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat")


@app.websocket("/ws/pong/{client_id}")
async def websocket_pong_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    await manager.broadcast(json.dumps({"info": f"Client #{client_id} entered game"}))
    try:
        while True:
            await manager.broadcast(json.dumps(CACHE))
            data = await websocket.receive_text()
            if data == "ArrowUp":
                print("UP")
                CACHE["pad1"]["top"] -= 5
            if data == "ArrowDown":
                print("DOWN")
                CACHE["pad1"]["top"] += 5
            # await manager.send_personal_message(f"You wrote: {data}", websocket)
            # await manager.broadcast(f"Client #{client_id} says: {data}")
            # await asyncio.sleep(0.033)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(json.dumps({"info": f"Client #{client_id} has left game"}))
    except RuntimeError:
        print(manager.active_connections)


@app.websocket("/ws/field/{client_id}")
async def websocket_field_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            # data = await websocket.receive_text()
            # print("->", data)
            # await manager.send_personal_message(f"You wrote: {data}", websocket)
            await asyncio.sleep(0.033)
            await manager.broadcast(json.dumps(CACHE))
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat")
    except RuntimeError:
        print("CLOSE")
