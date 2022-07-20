from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Message, Channel

class LoginForm(forms.Form):
  username = forms.CharField()
  password = forms.CharField( widget=forms.PasswordInput() )
  
class SignUpForm(UserCreationForm):
  email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')
  class Meta:
    model=User
    fields = ('username', 'password1','password2' ,'email',)
class MessageForm(forms.ModelForm):
  class Meta:
    model = Message
    fields = ('text',)
    widgets = {'text':forms.Textarea(attrs={'placeholder':'Type a message here', 'id':'message', 'autocomplete':'off', 'rows':'1', 'oninput':'auto_grow(this)' }) }
    
class ChannelForm(forms.ModelForm):
  class Meta:
    model = Channel
    fields = ('title', 'desc',)
    labels = {
      'title': 'Title',
      'desc':'Description',
    }

class SearchForm(forms.Form):
  search_term = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Type a message here'}))
    

