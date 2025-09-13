import requests
from rest_framework import viewsets, status, serializers
from rest_framework.response import Response
from .models import Pokemon, Treinador, Equipe
from .serializers import PokemonSerializer, TreinadorSerializer, EquipeSerializer, EquipeCreateUpdateSerializer

class PokemonViewSet(viewsets.ModelViewSet):
   queryset = Pokemon.objects.all()
   serializer_class = PokemonSerializer
   
   def perform_create(self, serializer):
      busca = serializer.validated_data.get('busca_pokedex').lower()

      #Etapa aonde acontece a interação com a API e a validação da busca
      try: 
         response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{busca}")
         response.raise_for_status()
         data = response.json()
      except requests.RequestException:
         raise serializers.ValidationError(f"Não foi possível encontrar o Pokémon {busca}.")
      
      #Devido a estruturação do Pokeapi, é necessário buscar de forma mais específica para descobrir os tipos do pokemon
      tipos_encontrados = []
      for item_tipo in data['types']: #Ele busca todos os atributos types 
         nome_do_tipo = item_tipo['type']['name'] #E puxa a informação nome de cada um deles
         tipos_encontrados.append(nome_do_tipo) #E então ele junta tudo em uma lista
      tipos_str = ','.join(tipos_encontrados) #E guarda tudo como string
      
      #Etapa aonde é salvo todos as informações do Pokémon
      pokemon, created = Pokemon.objects.update_or_create(
         id=data['id'],
         defaults={
            'nome':data['name'],
            'altura':data['height'],
            'peso':data['weight'],
            'tipo':tipos_str,
            'sprite_url':data['sprites']['front_default']
         }
      )
      
class TreinadorViewSet(viewsets.ModelViewSet):
   queryset = Treinador.objects.all()
   serializer_class = TreinadorSerializer
   
class EquipeViewSet(viewsets.ModelViewSet):
   queryset = Equipe.objects.all()
   serializer_class = EquipeSerializer
   
   def create(self, request, *args, **kwargs):
      create_serializer = EquipeCreateUpdateSerializer(data=request.data)
      if not create_serializer.is_valid():
         return Response(create_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
      treinador = create_serializer.validated_data['treinador']
      
      if treinador.equipe_set.count() >= 6:
         return Response(
            {"Erro":"O limite de 6 pokemons foi atingido"},
            status=status.HTTP_400_BAD_REQUEST
         )
      return super().create(request,*args,**kwargs)
   
   def get_serializer_class(self):
      if self.action in ['create','update','partial_update']:
         return EquipeCreateUpdateSerializer
      return EquipeSerializer