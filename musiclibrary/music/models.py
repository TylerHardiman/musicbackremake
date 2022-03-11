from django.db import models

# Create your models here.

class Song(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    release_date = models.CharField(max_length=50)

class AddSong(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    artist = models.CharField(max_length=100, blank=True, default='')
    album = models.CharField(max_length=100, blank=True, default='')
    genre = models.CharField(max_length=100, blank=True, default='')
    release_date = models.CharField(max_length=100, blank=True, default='')


    class Meta:
        db_table = 'music_library_database'