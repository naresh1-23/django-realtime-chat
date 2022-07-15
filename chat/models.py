from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
class Room(models.Model):
    room_number = models.CharField(max_length=10000)
    password = models.CharField(max_length=1000)

    def __str__(self):
        return self.room_number


class Message(models.Model):
    messages = models.CharField(max_length=1000000)
    date = models.DateField(default=datetime.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.messages