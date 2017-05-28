from django.shortcuts import render
from EmulationApplication.models import User, Song
from EmulationApplication.serializers import SongSerializer, UserSerializer
from django.http import Http404, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

def index(request):
    return HttpResponse('''<h1>Hello World!</h1>''')

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
