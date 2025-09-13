from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Pokemon, Treinador, Equipe

class PokemonSerializer(serializers.ModelSerializer):
   busca_pokedex = serializers.CharField(write_only=True,help_text="Nome ou ID para ser buscado na pokedex")
   sprite_url = serializers.URLField(read_only=True)
   class Meta:
      model = Pokemon
      fields = ['busca_pokedex','id','nome','altura','peso','tipo','sprite_url']
      read_only_fields = ['id','nome','altura','peso','tipo','sprite_url']
   
class EquipeSerializer(serializers.ModelSerializer):
   pokemon = PokemonSerializer(read_only=True)
   class Meta:
      model = Equipe
      fields = ['id','pokemon','apelido']
   
class TreinadorSerializer(serializers.ModelSerializer):
   equipe = EquipeSerializer(
      source='equipe_set',
      many=True,
      read_only=True)
   
   class Meta:
      model = Treinador
      fields = ['id','nome','equipe']

class UserSerializer(serializers.ModelSerializer):
   password = serializers.CharField(write_only=True)
   class Meta:
      model = User
      fields = ('username','password')
   def create(self,validated_data):
      user = User.objects.create_user(
         username=validated_data['username'],
         password=validated_data['password']
      )
      Treinador.objects.create(user=user)
      return user

class EquipeCreateUpdateSerializer(serializers.ModelSerializer):
   class Meta:
      model = Equipe
      fields = ['treinador','pokemon','apelido']