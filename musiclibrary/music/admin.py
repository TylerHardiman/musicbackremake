from django.contrib import admin
from .models import Song
from .models import AddSong

# Register your models here.
admin.site.register(Song)
admin.site.register(AddSong)