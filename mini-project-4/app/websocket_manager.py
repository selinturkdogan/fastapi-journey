from fastapi import WebSocket


class ConnectionManager:
    def __init__(self):
        self.active_connections = {}

    async def connect(self, poll_id: int, websocket: WebSocket):
        await websocket.accept()

        if poll_id not in self.active_connections:
            self.active_connections[poll_id] = []

        self.active_connections[poll_id].append(websocket)

    def disconnect(self, poll_id: int, websocket: WebSocket):
        if poll_id in self.active_connections:
            self.active_connections[poll_id].remove(websocket)

    async def broadcast(self, poll_id: int, message: dict):
        if poll_id in self.active_connections:

            disconnected = []

            for connection in self.active_connections[poll_id]:
                try:
                    await connection.send_json(message)
                except:
                    disconnected.append(connection)

            for connection in disconnected:
                self.disconnect(poll_id, connection)


manager = ConnectionManager()