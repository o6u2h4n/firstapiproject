from django.shortcuts import render
from .models import Events, Posts
from .serializers import LeadSerializer, PostSerializer
from rest_framework import generics, viewsets
import requests

class LeadListCreate(generics.ListCreateAPIView):
    queryset = Events.objects.all()
    serializer_class = LeadSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all().order_by('title')
    serializer_class = PostSerializer

def home(request):
    response = requests.get('http://127.0.0.1:8000/posts/')
    data = response.json()
    return render (request, 'home.html',{'data':data})