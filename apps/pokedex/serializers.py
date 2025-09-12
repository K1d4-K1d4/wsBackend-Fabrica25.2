from rest_framework import serializers
from .models import Pokemon, Treinador, Equipe

class PokemonSerializer(serializers.ModelSerializer):
   class Meta:
      model = Pokemon
      fields = ['id','nome','altura','peso','tipo']
      read_only_fields = ['altura','peso','tipo']
   
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

class AdicionarPokemonSerializer(serializers.Serializer):
   pokemon_id = serializers.IntegerField()
   apelido = serializers.CharField(max_length=100, required=False, allow_blank=True)