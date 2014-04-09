from django.contrib.auth.models import User, Group
from pickupapp.models import Sport, Location, Game
from rest_framework import serializers
from datetime import datetime

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
		
class SportSerializer(serializers.Serializer): 
    title = serializers.CharField(max_length=100)
    created = serializers.DateTimeField(default=datetime.now)
	
    class Meta:
        model = Sport
        #ordering = ['created']
        fields = ('title','created')

class LocationSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)	
    created = serializers.DateTimeField(default=datetime.now)
	
    class Meta:
        model = Location
        #ordering = ['created']
        fields = ('title','created')

class GameSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=300)
    capacity = serializers.IntegerField()
    creator = serializers.RelatedField()
    sport = serializers.RelatedField()
    location = serializers.RelatedField()
    time = serializers.DateTimeField()
    duration = serializers.IntegerField() # should this only be hours?
    created = serializers.DateTimeField(default=datetime.now)
	
    class Meta:
        model = Game
        #ordering = ['time']
        fields = ('title','description','capacity','creator','sport','location','time','duration','created')
	