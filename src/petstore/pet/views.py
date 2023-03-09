from django.shortcuts import render
from .serializers import PetSerializer
from .models import Pet, Breed, User, Image
from rest_framework import viewsets, permissions
# Create your views here.
class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer