import requests
from rest_framework import viewsets, status, serializers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Pokemon, Treinador, Equipe
from .serializers import PokemonSerializer, TreinadorSerializer, EquipeSerializer, EquipeCreateUpdateSerializer


class PokemonViewSet(viewsets.ModelViewSet):
   queryset = Pokemon.objects.all()
   serializer_class = PokemonSerializer
   
   def create(self, request, *args, **kwargs):
      serializer = self.get_serializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      busca = serializer.validated_data.get('busca_pokedex').lower()

      try: 
         response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{busca}")
         response.raise_for_status()
         data = response.json()
      except requests.RequestException:
         raise serializers.ValidationError(f"Não foi possível encontrar o Pokémon '{busca}'.")
      
      tipos_lista = [t['type']['name'] for t in data['types']]
      tipos_str = ','.join(tipos_lista)
      
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
      
      status_code = status.HTTP_201_CREATED if created else status.HTTP_200_OK
      response_serializer = self.get_serializer(pokemon)
      return Response(response_serializer.data, status=status_code)
         
class TreinadorViewSet(viewsets.ModelViewSet):
   serializer_class = TreinadorSerializer
   permission_classes = [IsAuthenticated]
   
   def get_queryset(self):
      return Treinador.objects.filter(user=self.request.user)
   
class EquipeViewSet(viewsets.ModelViewSet):
   serializer_class = EquipeSerializer
   permission_classes = [IsAuthenticated]
   
   def get_queryset(self):
      return Equipe.objects.filter(treinador__user=self.request.user)
   
   def perform_create(self,serializer):
      treinador = Treinador.objects.get(user=self.request.user)
      if treinador.equipe_set.count() >= 6:
         raise serializers.ValidationError("A equipe já está lotada, máximo de 6 pokemons")
      serializer.save(treinador=treinador)

   def get_serializer_class(self):
      if self.action in ['create','update','partial_update']:
         return EquipeCreateUpdateSerializer
      return EquipeSerializer