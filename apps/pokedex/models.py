from django.db import models

# Create your models here.
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
   nome = models.CharField(max_length=100)
   pokemons = models.ManyToManyField(Pokemon, through='Equipe', related_name='treinadores')
   
   def __str__(self):
      return self.nome
   
#Classe que será usada para registrar uma equipe criada pelo usuário   
class Equipe(models.Model):
   treinador = models.ForeignKey("Treinador", on_delete=models.CASCADE)
   pokemon = models.ForeignKey("Pokemon", on_delete=models.CASCADE)
   apelido = models.CharField(max_length=100,blank=True,null=True)
   
   #Classe que impede o usuário de inserir o mesmo pokémon mais de uma vez na mesma equipe
   class Meta:
      unique_together = ('treinador', 'pokemon')#
      
   def __str__(self):
      return f"{self.pokemon.nome} na equipe de {self.treinador.nome}"