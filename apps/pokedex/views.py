from django.shortcuts import render
from .models import Pokemon
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import generics

def pokemon_list_view(request):
   pokemons = Pokemon.objects.all().order_by('id')
   return render(request, 'pokedex/pokemon_list.html', {'pokemons': pokemons})

class RegistrationView(generics.CreateAPIView):
   queryset = User.objects.all()
   serializer_class = UserSerializer