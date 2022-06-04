from django.db import models

# Create your models here.
class Autor(models.Model):
    nome = models.CharField(max_length=30)
    telefone = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nome
    
class Editora(models.Model):
   # id = models.IntegerField()
   descricao = models.CharField(max_length=100)
   telefone = models.IntegerField(15)
   
   def __str__(self):
       return self.descricao

class Livro(models.Model):
    Titulo = models.CharField(max_length=150)
    paginas = models.IntegerField()
    isbn = models.CharField(max_length=40)
    Autores = models.ManyToManyField(Autor)
    editora = models.ForeignKey(Editora, on_delete= models.CASCADE)
    
    
   
    def __str__(self):
        return self.Titulo