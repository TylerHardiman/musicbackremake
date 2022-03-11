from rest_framework import serializers
from .models import Song
from .models import AddSong



class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = [ 'id', 'title', 'artist', 'album', 'genre', 'release_date']
        

#Deciding to go this route going through the django REST framework documentation provided
        
class AddSongSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100, blank=True, default='')
    artist = serializers.CharField(max_length=100, blank=True, default='')
    album = serializers.CharField(max_length=100, blank=True, default='')
    genre = serializers.CharField(max_length=100, blank=True, default='')
    release_date = serializers.CharField(max_length=100, blank=True, default='')
    
    def create(self, validated_data):
        """
        Create and return a new `AddSong` instance, given the validated data.
        """
        return AddSong.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `AddSong` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.artist = validated_data.get('artist', instance.artist)
        instance.album = validated_data.get('album', instance.album)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.save()
        return instance
