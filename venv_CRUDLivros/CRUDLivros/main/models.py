from django.db import models

# Create your models here.
class Autor(models.Model):
    nome = models.CharField(max_length=30)
    telefone = models.CharField(max_length=30)
    

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    Isbn = models.CharField(max_length=30)
    ano = models.IntegerField(max_length=10)
    edicao = models.IntegerField(max_length=10)
    
class Editorea(models.Model):
   # id = models.IntegerField()
   descricao = models.CharField(max_length=100)
   telefone = models.IntegerField(15)
   
   