from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer.as_asgi()),
]

# url(r'^ws/chat/(?P<room_name>[^/]+)/$'
# re_path(r'ws/chat/(?P<room_name>\w+)/$'