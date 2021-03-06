from .models import Song
from .models import AddSong
from .serializers import AddSongSerializer
from .serializers import SongSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

# Create your views here.
class SongList(APIView):
    
    def get(self, request):
        song = Song.objects.all()
        serializer = SongSerializer(song, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def add_song_list(request):
    """
    List all code AddSong, or create a new AddSong.
    """
    if request.method == 'GET':
        add_song_list = AddSong.objects.all()
        serializer = AddSongSerializer(add_song_list, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AddSongSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
def add_song_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        add_song_detail = AddSong.objects.get(pk=pk)
    except AddSong.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AddSongSerializer(add_song_detail)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AddSongSerializer(add_song_detail, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        AddSong.delete()
        return HttpResponse(status=204)

