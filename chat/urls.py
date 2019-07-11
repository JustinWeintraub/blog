from django.urls import path
from .views import ChatBoardView
urlpatterns = [
path('chat/', ChatBoardView.as_view(), name='chat-board'),
]
