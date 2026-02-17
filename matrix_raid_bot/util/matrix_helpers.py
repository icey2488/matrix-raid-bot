# Placeholder Matrix service wrapper

class MatrixService:
    def __init__(self, client):
        self._client = client

    async def send_text(self, room_id: str, body: str):
        pass