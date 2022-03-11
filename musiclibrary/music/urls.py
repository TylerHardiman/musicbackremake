from django.urls import path
from . import views

urlpatterns = [
    path('music/', views.SongList.as_view()),
    path('AddSong/', views.add_song_list),
    path('AddSong/<int:pk>/', views.add_song_detail),
]