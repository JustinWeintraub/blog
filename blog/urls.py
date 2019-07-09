#url for blog to work
from . import views #. is current
from .views import (
PostListView, PostDetailView, PostCreateView,
PostUpdateView, PostDeleteView, UserPostListView
)
from django.urls import path
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'), #/home is empty works
    #was views.home
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    #pk primary key, what detailed view expects it to be
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    path('about/', views.about, name='blog-about'),
]
