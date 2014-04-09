from django.contrib.auth.models import User, Group
from django.db import models
from datetime import datetime

'''class Member(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    password = models.CharField(_('password'), max_length=256)'''

class Sport(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(default=datetime.now)
    
    class Meta:
        ordering = ['created']

class Location(models.Model):
    title = models.CharField(max_length=100)	
    created = models.DateTimeField(default=datetime.now)
    
    class Meta:
        ordering = ['created']

class Game(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    capacity = models.IntegerField()
    creator = models.ForeignKey(User,related_name='creator')
    sport = models.ForeignKey(Sport,related_name='sport')
    location = models.ForeignKey(Location,related_name='location')
    time = models.DateTimeField()
    duration = models.IntegerField() # should this only be hours?
    created = models.DateTimeField(default=datetime.now)
    
    class Meta:
        ordering = ['time']