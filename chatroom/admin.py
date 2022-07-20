from django.contrib import admin
from .models import Member, Message, Channel

# Register your models here.

@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
  list_display = ('title', 'desc')
  prepopulated_fields = {'slug':('title',) }

  
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
  list_display = ('user', 'photo')

  
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
  list_display = ('author', 'channel', 'text')

  
