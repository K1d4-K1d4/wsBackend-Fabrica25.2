from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views
from .viewsets import PokemonViewSet, TreinadorViewSet, EquipeViewSet

router = DefaultRouter()
router.register(r'pokemons', PokemonViewSet, basename='pokemon')
router.register(r'treinadores', TreinadorViewSet, basename='treinador')
router.register(r'equipes', EquipeViewSet, basename='equipe')

urlpatterns = [
#Rotas das interfaces WEB
   path('', views.auth_view, name='auth-page'),
   path('register/', views.register_view, name='register'),
   path('login/', views.login_view, name='login'),
   path('logout/', views.logout_view, name='logout'),
   path('buscar/', views.buscar_pokemon, name='buscar-pokemon'),
   path('equipe/', views.minha_equipe, name='minha-equipe'),
   path('equipe/remover/<int:equipe_id>/', views.remover_pokemon, name='remover-pokemon'),
   path('conta/apagar/', views.delete_account_view, name='delete-account'),
#Rotas da API
   path('api/', include(router.urls)),
   path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]