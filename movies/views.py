from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Movies, Actor
from .serializers import MovieSerializer,ActorSerializer

# Create your views here
# ViewSets define the view behavior

class MoviesViewSet(ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer