from rest_framework.serializers import ModelSerializer
from .models import Movies,Actor

# Serializers define the API representation

class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'


class ActorSerializer(ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'