from channels.generic.websocket import WebsocketConsumer
import json
from .models import Messages,userChannel
from asgiref.sync import async_to_sync
from django.contrib.auth.models import  User
class DashboardConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
       
    
        
        
        try:
            user = userChannel.objects.get( user = self.scope.get('user'))
            user.channel_name = self.channel_name
            user.save()
            
        except:
            new_connection = userChannel()
            my_user = self.scope.get('user')
            new_connection.user = my_user
            new_connection.channel_name = self.channel_name
            new_connection.save()
        
        
        
        #print(self.channel_layer)
        #print(self.channel_layer.channels)
        async_to_sync(self.channel_layer.group_add)('Study' , self.channel_name)
        
        
        
        
        
        
        
    def receive(self, text_data):
        data = json.loads(text_data)
        message_val = data.get('message')
        message_type = data.get('type')
        user = self.scope.get('user')
        createmodel = Messages()
        
        receiver_id = self.scope.get('url_route').get('kwargs').get('id')
        receiver = User.objects.get(id=receiver_id)
        createmodel.from_user = user
        createmodel.to_user = receiver
        createmodel.data = message_val
        createmodel.save()
        try:
            data = {
                'type' : 'receive_func',
                'message_type' : 'new_message',
                'value' : message_val
            }
            to_user = userChannel.objects.get(user = receiver)
        
            async_to_sync(self.channel_layer.send)(to_user.channel_name , data)
        except:
            pass

        

    def disconnect(self,code):
        print('disconnected')
    
    def receive_func(self,data):
        print(data)
        
        my_data= json.dumps(data)
        self.send(my_data)
        
    