from django.contrib import admin
from .models import Battle, Monster, Character

# Register your models here.
admin.site.register(Monster)
admin.site.register(Character)
admin.site.register(Battle)