from django.db import models
from django.contrib.auth import get_user_model
import datetime
import json

# Create your models here.
class Monster(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Character(models.Model):
    name = models.CharField(max_length=100)
    strength = models.IntegerField(null=False, default=10)
    dex = models.IntegerField(null=False, default=10)
    con = models.IntegerField(null=False, default=10)
    inteligence = models.IntegerField(null=False, default=10)
    wis = models.IntegerField(null=False, default=10)
    cha = models.IntegerField(null=False, default=10)
    armor_class = models.IntegerField(null=False, default=10)
    hp = models.IntegerField(null=False, default=10)

    def __str__(self):
        return self.name
    
class Battle(models.Model):

    created_by = models.CharField(null=False, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    participant_monsters = models.ForeignKey(Monster, null=True, blank=True, on_delete=models.SET_NULL)
    participant_characters = models.ForeignKey(Character, null=True, blank=True, on_delete=models.SET_NULL)
