from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.db import IntegrityError
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import  make_password
from django.contrib.auth.hashers import  check_password
from django.core.files.storage import FileSystemStorage
import json

def send(request):
    message = request.POST['message']
    user = User.objects.get(id=request.POST['user'])
    deck = Deck.objects.get(id=request.POST['deck_id'])
    new_message = Message.objects.create(value=message, deck=deck, user=user)
    new_message.save()
    return HttpResponse("Message sent successfully!")


def getMessages(request,pk):
    messages = Message.objects.filter(deck__id=pk)
    data =[]
    for ms in messages:
        data.append({"value":ms.value, "date":ms.date, "user":ms.user.username})
    return JsonResponse({"messages":data, })

def deckauth(request, pk):
    room_details = Deck.objects.get(id=pk)
    sk = SecurityKeys.objects.get(deck=room_details)
    if request.method == 'POST':
        passw = request.POST['keys']
        flag= check_password(passw , sk.keys)
        if flag:
            room_details.users.add(request.user.id)
            room_details.save()
            return HttpResponseRedirect(reverse('group_chat',args=[pk]))
        else:
            context = {'room_details': room_details,'message':"Wrong Keys"}
            return render(request,'auth.html',context)
    else:
        return render(request,'auth.html',{'room_details':room_details})
    

@csrf_exempt
def postedit(request):
    if request.method != "PUT":
        return JsonResponse({"error":"PUT request required."},status=400)

    data = json.loads(request.body)
    editbutton = data.get("editbutton", "")   
    content = data.get("content", "")
    deck = Deck.objects.get(id= editbutton)
    if content:
        deck.title = content
        deck.save()
    return JsonResponse({'message':'Post edited'})


def group_chat(request, pk):
    deck = Deck.objects.get(id= pk)
    groups = set(Deck.objects.filter(Q(users=request.user) |Q(group_admin=request.user)))
    context = {'deck':deck,'groups':groups,'pk':pk}
    return render(request,'base.html',context)

@login_required
def index(request):
    groups =  set(Deck.objects.filter(Q(users=request.user) |Q(group_admin=request.user)))
    suggested_groups = set(Deck.objects.exclude(Q(users=request.user) |Q(group_admin=request.user)))
    
    return render(request,'base.html',{'groups':groups,'suggested_groups':suggested_groups,})

@login_required
def create(request):
    if request.method == 'POST' and request.FILES['upload']:
        title = request.POST['title']
        description = request.POST['description']
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        deck = Deck.objects.create(group_admin=request.user,users_limit=5,
                            title=title,description=description)
        user =  User.objects.get(username=request.user)
        deck.group_profile.save(upload.name, upload)
        deck.users.add(user)
        deck.save()
        ps = make_password(request.POST['password'])
        sk = SecurityKeys.objects.create(deck=deck, keys= ps )
        sk.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request,'create.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'login.html')
    else:
        return render(request,'login.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "register.html")