from django.db import models

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