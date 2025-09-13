from django.db import models
from django.contrib.auth.models import User

class Pokemon(models.Model):
   id = models.IntegerField(primary_key=True)
   nome = models.CharField(max_length=255, unique=True)
   altura = models.IntegerField()
   peso = models.IntegerField()
   tipo = models.CharField(max_length=50)
   sprite_url = models.URLField(max_length=500, blank=True, null=True)
   
   def __str__(self):
      return self.nome.capitalize()

class Treinador(models.Model):
   user = models.OneToOneField(User,on_delete=models.CASCADE)
   pokemons = models.ManyToManyField(Pokemon, through='Equipe', related_name='treinadores')
   
   def __str__(self):
      return self.user.username
   
class Equipe(models.Model):
   treinador = models.ForeignKey("Treinador", on_delete=models.CASCADE)
   pokemon = models.ForeignKey("Pokemon", on_delete=models.CASCADE)
   apelido = models.CharField(max_length=100,blank=True,null=True)
   
   class Meta:
      unique_together = ('treinador', 'pokemon')
      
   def __str__(self):
      return f"{self.pokemon.nome} na equipe de {self.treinador.user.username}"