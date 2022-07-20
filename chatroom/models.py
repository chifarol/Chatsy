from django.db import models
from django.urls import reverse;
from django.contrib.auth.models import User

# Create your models here.

class Member(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='member')
  photo = models.ImageField(blank=True, null=True )
  def __str__(self):
    return self.user.username

class Channel(models.Model):
  title = models.CharField(max_length=100)
  slug = models.SlugField(max_length=200,unique=True)
  desc = models.CharField(max_length=250)
  created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='channels_created', null=True)

  channel_pic = models.ImageField(blank=True, null=True)
  members = models.ManyToManyField(Member, related_name='channels', blank=True)
  def image_url(self):
    if self.channel_pic and hasattr(self.channel_pic, 'url'):
      return self.channel_pic.url
    else:
      return '/static/chatroom/temp-images/no_image.png'
      
  def get_absolute_url(self):
    return reverse('chatroom:channel_detail', args=[self.slug])
  def __str__(self):
    return self.title
  def channel_abv(self):
    abv = ''
    slug=str(self.slug)
    slug_split = slug.split('-')
    for x in slug_split:
      abv+=x[0]
    return abv[:2]
      

class Message(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_messages')
  channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name='channel_messages')
  text = models.CharField(max_length=250)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.author.username
    
  class Meta:
    ordering=['created']
  
