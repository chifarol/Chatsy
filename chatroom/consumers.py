import json
from channels.generic.websocket import WebsocketConsumer
from .models import Channel
from .forms import MessageForm
from django.contrib.auth.models import User
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
  def connect(self):
    self.room_name = self.scope['url_route']['kwargs']['room_name']
    self.room_group_name = 'chat_%s' % self.room_name
    # Join room group
    async_to_sync(self.channel_layer.group_add)(
      self.room_group_name,
      self.channel_name
    )
    self.accept()

  def disconnect(self, close_code):
    # Leave room group
    async_to_sync(self.channel_layer.group_discard)(
      self.room_group_name,
      self.channel_name
    )

  def receive(self, text_data):
    text_data_json = json.loads(text_data)
    message = text_data_json['message']
    username = text_data_json['username']
    channel_slug = text_data_json['channel-slug']
    
    channel = Channel.objects.get(slug=channel_slug)
    author = User.objects.get(username=username)
    
    msg_form = MessageForm(data={'text':message})
    if msg_form.is_valid():
      msg_instance = msg_form.save(commit=False)
      msg_instance.channel = channel
      msg_instance.author = author
      msg_instance.save()
      if author.member.photo.url:
        author_photo_url = author.member.photo.url
      else:
        author_photo_url="{% static 'chatroom/temp-images/no_images.png' %}"
      msg_time = msg_instance.created.strftime("%H:%M")
      msg_date = msg_instance.created.strftime("%b %d %Y")
      msg_container = {
        'message': msg_instance.text,
        'author_photo_url':author_photo_url,
        'username':username,
        'msg_date':msg_date,
        'msg_time':msg_time,
      }
      # Send message to room group
      async_to_sync(self.channel_layer.group_send)(
        self.room_group_name,
        {
          'type': 'chat_message',
          'msg_container': msg_container
          }
        )
  # Receive message from room group
  def chat_message(self, event):
    msg_container = event['msg_container']
    # Send message to WebSocket
    self.send(text_data=json.dumps({
       'msg_container': msg_container
    })) 