from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'main-home' ),
    path('create-room/', views.createroom, name='create-room'),
    path('join-room/', views.joinroom, name = 'join-room'),
    path('room/<int:id>', views.chatbox, name = 'chat-room'),
]