from django.contrib.auth.models import User, Group
from django.http import HttpResponse, HttpRequest
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from pickupapp.models import Sport, Location, Game
from pickupapp.serializers import UserSerializer, GroupSerializer, SportSerializer, LocationSerializer, GameSerializer
import django_filters


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def list(self, request):
        return HttpResponse(content='YATAH')
    
    def create(self, request):
        return HttpResponse()
    
    def retrieve(self, request, pk=None):
        return HttpResponse(content='{}')
    
    def update(self, request, pk=None):
        return HttpResponse()
    
    def partial_update(self, request, pk=None):
        return HttpResponse()
    
    def destroy(self, request, pk=None):
        return HttpResponse()


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    
    def list(self, request):
        return HttpResponse(content='YATAH')
    
    def create(self, request):
        return HttpResponse()
    
    def retrieve(self, request, pk=None):
        return HttpResponse(content='{}')
    
    def update(self, request, pk=None):
        return HttpResponse()
    
    def partial_update(self, request, pk=None):
        return HttpResponse()
    
    def destroy(self, request, pk=None):
        return HttpResponse()


class SportViewSet(viewsets.ModelViewSet):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer
    
    def list(self, request):
        return HttpResponse(content='YATAH')
    
    def create(self, request):
        return HttpResponse()
    
    def retrieve(self, request, pk=None):
        return HttpResponse(content='{}')
    
    def update(self, request, pk=None):
        return HttpResponse()
    
    def partial_update(self, request, pk=None):
        return HttpResponse()
    
    def destroy(self, request, pk=None):
        return HttpResponse()


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    
    def list(self, request):
        return HttpResponse(content='YATAH')
    
    def create(self, request):
        return HttpResponse()
    
    def retrieve(self, request, pk=None):
        return HttpResponse(content='{}')
    
    def update(self, request, pk=None):
        return HttpResponse()
    
    def partial_update(self, request, pk=None):
        return HttpResponse()
    
    def destroy(self, request, pk=None):
        return HttpResponse()


class GameFilter(django_filters.FilterSet):
    class Meta:
        model = Game
        fields = ['title','description','capacity','creator','sport','location','time','duration','created']


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    filter_class = GameFilter
    
    def list(self, request):
        return HttpResponse(content='YATAH')
    
    def create(self, request):
        return HttpResponse()
    
    def retrieve(self, request, pk=None):
        return HttpResponse(content='{}')
    
    def update(self, request, pk=None):
        return HttpResponse()
    
    def partial_update(self, request, pk=None):
        return HttpResponse()
    
    def destroy(self, request, pk=None):
        return HttpResponse()