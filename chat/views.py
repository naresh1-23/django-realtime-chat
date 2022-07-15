from django.shortcuts import render, redirect
from .forms import RoomCreateform, RoomJoinform, MessageForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Room, Message
# Create your views here.
def home(request):
    return render(request, 'chat/home.html')

@login_required
def createroom(request):
    if request.method == 'POST':
        form = RoomCreateform(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            confirm_passsword = form.cleaned_data.get('confirm_password')
            if password == confirm_passsword:
                form.save()
                messages.success(request, f'Room created')
                return redirect('join-room')
            else:
                messages.warning(request, f'Password didnt matched')
                return redirect('create-room')
    else:
        form = RoomCreateform()
    return render(request, 'chat/createroom.html', { 'form':form })

@login_required
def joinroom(request):
    if request.method== 'POST':
        form = RoomJoinform(request.POST)
        if form.is_valid():
            room = form.cleaned_data.get('room_number')
            password = form.cleaned_data.get('password')
            existroom = Room.objects.all().filter(room_number= room).count()
            if existroom!=0:
                roomname = Room.objects.get(room_number= room)
                if roomname.password == password:
                    room_id = roomname.id
                    return redirect('/room/'+str(room_id))
                else:
                    messages.warning(request, f'Password didnt matched')
                    return redirect('join-room')
            else:
                messages.warning(request, f"Room doesn't exist")
                return redirect('join-room')
    else:
        form = RoomJoinform()
    return render(request, 'chat/createroom.html', { 'form':form })


@login_required
def chatbox(request, id):
    if request.method == 'POST':
        room_id = id
        room = Room.objects.get(pk = room_id)
        chats = Message.objects.all()
        form = MessageForm(request.POST, instance=request.user)
        if form.is_valid():
            msg = form.cleaned_data.get('message')
            m = Message(messages = msg, author = request.user, room = room)
            m.save()
            return redirect('/room/'+str(room_id))
    form = MessageForm()
    room_id = id
    room = Room.objects.get(pk = room_id)
    chats = Message.objects.all()
    return render(request, 'chat/chatbox.html', {'form':form,'chats':chats, 'room':room })