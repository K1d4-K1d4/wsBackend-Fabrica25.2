import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Pokemon, Treinador, Equipe
from .forms import UserRegistrationForm, UserLoginForm
from rest_framework import generics
from .serializers import UserSerializer
from django.contrib.auth.models import User

class RegistrationView(generics.CreateAPIView):
   queryset = User.objects.all()
   serializer_class = UserSerializer

def auth_view(request):
   if request.user.is_authenticated:
      return redirect('minha-equipe')
   
   register_form = UserRegistrationForm()

   users = User.objects.order_by('username')
   username_choices = [(user.username, user.username) for user in users]
   login_form = UserLoginForm(choices=username_choices)

   context = {
      'register_form': register_form,
      'login_form': login_form,
   }
   return render(request, 'pokedex/auth.html', context)
   
def register_view(request):
   if request.method == 'POST':
      form = UserRegistrationForm(request.POST)
      if form.is_valid():
         user = form.save()
         login(request, user)
         return redirect('minha-equipe')
      else:
         for field, errors in form.errors.items():
            for error in errors:
               messages.error(request, error)
   return redirect('auth-page')

def login_view(request):
   if request.method == 'POST':
      users = User.objects.order_by('username')
      username_choices = [(user.username, user.username) for user in users]
      form = UserLoginForm(request.POST, choices=username_choices)

      if form.is_valid():
         username = form.cleaned_data['username']
         password = form.cleaned_data['password']
         user = authenticate(request, username=username, password=password)
         if user is not None:
            login(request, user)
            return redirect('minha-equipe')
         else:
            messages.error(request, 'Senha inválida para o usuário selecionado.')
      else:
         messages.error(request, 'Formulário inválido.')

   return redirect('auth-page')

def logout_view(request):
   logout(request)
   return redirect('auth-page')

@login_required
def buscar_pokemon(request):
   context = {}
   treinador = get_object_or_404(Treinador, user=request.user)

   if request.method == 'POST':
      pokemon_id = request.POST.get('pokemon_id')
      apelido = request.POST.get('apelido')
      pokemon = get_object_or_404(Pokemon, id=pokemon_id)

      if treinador.equipe_set.count() < 6:
         _, created = Equipe.objects.get_or_create(
               treinador=treinador, 
               pokemon=pokemon,
               defaults={'apelido': apelido}
         )
         if created:
               context['success_message'] = f"{pokemon.nome.capitalize()} foi adicionado à sua equipe!"
         else:
               context['error'] = f"{pokemon.nome.capitalize()} já está na sua equipe."
      else:
         context['error'] = "Sua equipe já está cheia!"
      
      # Re-fetch the pokemon to get formatted values if needed
      context['pokemon'] = pokemon
      # Formatar altura e peso para o contexto, mesmo se o pokemon já existir
      context['pokemon'].altura_cm = pokemon.altura * 10
      context['pokemon'].peso_kg = round(pokemon.peso / 10, 1)

   query = request.GET.get('q')
   if query:
      context['query'] = query
      try:
         pokemon = Pokemon.objects.get(nome=query.lower())
         context['pokemon'] = pokemon
         context['pokemon'].altura_cm = pokemon.altura * 10
         context['pokemon'].peso_kg = round(pokemon.peso / 10, 1)
      except Pokemon.DoesNotExist:
         try:
            response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{query.lower()}")
            response.raise_for_status()
            data = response.json()
            tipos_lista = [t['type']['name'] for t in data['types']]
            
            # Converte altura e peso do PokeAPI para salvar no modelo
            altura_dm = data['height']
            peso_hg = data['weight']
            
            pokemon, _ = Pokemon.objects.update_or_create(
               id=data['id'],
               defaults={
                  'nome': data['name'], 'altura': altura_dm,
                  'peso': peso_hg, 'tipo': ','.join(tipos_lista),
                  'sprite_url': data['sprites']['front_default']
               }
            )
            context['pokemon'] = pokemon
            # Adiciona os valores formatados ao contexto
            context['pokemon'].altura_cm = altura_dm * 10
            context['pokemon'].peso_kg = round(peso_hg / 10, 1)

         except requests.RequestException:
            context['error'] = f"Pokémon '{query}' não encontrado na Pokédex Online."

   return render(request, 'pokedex/buscar_pokemon.html', context)

@login_required
def minha_equipe(request):
   treinador = get_object_or_404(Treinador, user=request.user)
   equipe = treinador.equipe_set.all().select_related('pokemon')
   
   context = {
      'treinador': treinador,
      'equipe': equipe,
   }
   return render(request, 'pokedex/minha_equipe.html', context)

@login_required
def remover_pokemon(request, equipe_id):
   treinador = get_object_or_404(Treinador, user=request.user)
   entrada_equipe = get_object_or_404(Equipe, id=equipe_id, treinador=treinador)
   
   if request.method == 'POST':
      entrada_equipe.delete()
      return redirect('minha-equipe')

   return redirect('minha-equipe')

@login_required
def delete_account_view(request):
   if request.method == 'POST':
      user = request.user
      logout(request)
      user.delete()
      return redirect('auth-page')
   return redirect('minha-equipe')