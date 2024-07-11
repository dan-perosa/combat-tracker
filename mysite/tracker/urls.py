from django.urls import path, include
from . import views

urlpatterns = [
    path('select_participants/', views.select_participants, name='select_participants'),
]
