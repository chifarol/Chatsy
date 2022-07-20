app_name = 'chatroom'
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('',views.home, name='home'),
  path('signup',views.signup_user, name='signup'),
  path('login',views.login_user, name='login'),
  path('logout',views.logout_user, name='logout'),
  path('create-channel',views.channel_create, name='channel_create'),
  path('search',views.search, name='search'),
  path('channel/join/<slug:slug>',views.join_channel, name='join_channel'),
  path('channel/leave/<slug:slug>',views.leave_channel, name='leave_channel'),
  path('channel/<slug:slug>',views.channel_detail, name='channel_detail'),
]
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)