from django import forms
from .models import Room , Message
class RoomCreateform(forms.ModelForm):
    room_number = forms.CharField(max_length=10000)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=1000)
    confirm_password = forms.CharField(widget=forms.PasswordInput(),max_length=1000 )

    class Meta:
        model = Room
        fields = ['room_number', 'password']

class RoomJoinform(forms.ModelForm):
    room_number = forms.CharField(max_length=10000)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=1000)

    class Meta:
        model = Room
        fields = ['room_number', 'password']

class MessageForm(forms.ModelForm):
    message  = forms.CharField(max_length=1000000)

    class Meta:
        model = Message
        fields = ['message']