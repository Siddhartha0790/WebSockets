from channels.generic.websocket import AsyncWebsocketConsumer
import json
class DashboardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print('connection established')
        await self.accept()
        
    async def disconnect(self, code):
        return await super().disconnect(code)
    
    async def receive(self, text_data):
        new_text_data = json.loads(text_data)
        message = new_text_data['message']
        sender = new_text_data['sender']
        
        print(message,sender)
        
        await self.send(text_data=json.dumps({
            'message' : message,
            'sender': sender
        }))
        
        