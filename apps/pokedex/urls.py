from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import PokemonViewSet, TreinadorViewSet, EquipeViewSet
from .views import pokemon_list_view  # ← Importe a nova view

router = DefaultRouter()
router.register(r'pokemons', PokemonViewSet)
router.register(r'treinadores', TreinadorViewSet)
router.register(r'equipes', EquipeViewSet)

urlpatterns = [
   path('', pokemon_list_view, name='pokemon-list'),  # ← Página principal
   path('api/', include(router.urls)),  # ← API REST
]