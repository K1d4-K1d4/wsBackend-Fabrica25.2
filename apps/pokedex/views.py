from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Pokemon

def pokemon_list_view(request):
   pokemons = Pokemon.objects.all().order_by('id')
   return render(request, 'pokedex/pokemon_list.html', {'pokemons': pokemons})