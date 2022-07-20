from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Channel, Member, Message
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LoginForm,MessageForm, ChannelForm, SearchForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your views here.


def signup_user(req):

    if req.method == 'POST':
        form = SignUpForm(req.POST)
        if form.is_valid():
          try:
            new_user = form.save()
            new_member = Member(user=new_user)
            new_member.save()
            return redirect('chatroom:login')
          except:
            messages.error(req, 'Something went wrong try again')
    else:
        form = SignUpForm()
    context = {'form': form, 'refer_to': 'signup', 'title': 'Sign Up'}

    return render(req, 'chatroom/parts/modal.html', context)


def logout_user(req):
    logout(req)
    return redirect('chatroom:login')


def login_user(req):
    if req.method == 'POST':
        form = LoginForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(req, username=username, password=password)
            if user is not None:
                login(req, user)
                return redirect('chatroom:home')
            else:
                messages.error(req, 'wrong username or password')

        else:
            messages.error(req, 'something went wrong, try again')

    else:
        form = LoginForm()

    context = {'form': form, 'refer_to': 'login', 'title': 'Log In'}

    return render(req, 'chatroom/parts/modal.html', context)

  
@login_required
def search(req):
  if req.method == 'GET':
    search_term=req.GET.get('search')
    search_form = SearchForm(data={'search_term':search_term})
    if search_form.is_valid():
      search_term=search_form.cleaned_data['search_term']
      # search_result = Channel.objects.filter( Q(desc__icontains=search_term))
      search_result = Channel.objects.filter(Q(title__icontains=search_term) | Q(desc__icontains=search_term))
      user_channel_list = req.user.member.channels.all()
      channel_list = Channel.objects.exclude(id__in=user_channel_list)
      context = {
        'previous': False,
        'channel_title': 'Search',
        'search_result': search_result,
        'search_term': search_term,
        'user_channel_list': user_channel_list,
        'channel_list': channel_list,
        }
      return render(req, 'chatroom/parts/search.html', {'context': context})
  return redirect('chatroom:home')
    
# | Q(channel_messages__text__icontains=search_term) 

  
@login_required
def channel_create(req):
    if req.method == 'POST':
      user= req.user
      member = Member.objects.get(user=user)
      form = ChannelForm(req.POST)
      if form.is_valid():
        form_instance = form.save(commit=False)
        form_instance.created_by = user
        form_instance.slug = slugify(form_instance.title)
        form_instance.save()
        form_instance.members.add(member)
        return redirect(form_instance)
      else:
          messages.error(req, 'something went wrong')
          return redirect('chatroom:home')

    else:
      return redirect('chatroom:home')


@login_required
def home(req):
    # user_id = req.user.id
    username = req.user.get_username()
    user_obj = User.objects.get(username=username)
    user_channel_list = user_obj.member.channels.all()
    channel_list = Channel.objects.exclude(id__in=user_channel_list)
    new_channel_form = ChannelForm()
    context = {
        'previous': False,
        'channel_title': 'Channels',
        'channel_list': channel_list,
        'user_channel_list': user_channel_list,
      'new_channel_form':new_channel_form
    }
    return render(req, 'chatroom/parts/home.html', {'context': context})

  
@login_required
def join_channel(req, slug):
  channel = Channel.objects.get(slug=slug)
  if req.user.member not in channel.members.all():
    channel.members.add(req.user.member)
    return redirect(channel)
  else:
    return redirect('chatroom:home')
  
@login_required
def leave_channel(req, slug):
  channel = Channel.objects.get(slug=slug)
  if req.user.member in channel.members.all():
    channel.members.remove(req.user.member)
    return redirect('chatroom:home')


@login_required
def channel_detail(req, slug):
  channel = Channel.objects.get(slug=slug)
  if req.user.member in channel.members.all():
    msg_form = MessageForm()
    context = {
        'previous': True,
        'channel_title': 'All Channels',
        'channel': channel,
        'msg_form': msg_form
    }
    return render(req, 'chatroom/parts/channel_detail.html', {'context': context})
  else:
    return redirect('chatroom:home')
    

