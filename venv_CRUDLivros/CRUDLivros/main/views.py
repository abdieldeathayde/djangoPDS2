from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView
from django.http import HttpResponse
from django.contrib import auth, messages
# from main import urls
from main.models import Livro, Autor, Editora
import datetime

# Create your views here.

def index(request):
    return HttpResponse("Você está na página index de livros")

def livro_list(request):
    lista_livros = Livro.objects.all()
    for livro in lista_livros:
        print(livro)
    return render(request, 'livros/livro_list.html', {'lista' : lista_livros})

def autor_list(request):
    lista_autores = Autor.objects.all()
    for autor in lista_autores:
        print(autor)
    return render(request, 'autor/autor_list.html', {'lista de autores': lista_autores})

def inserirAutor(request):
    #autores = Autor.objects.all()
    #for autor in autores:
     #   print(autor)
    #return render ("")
    novoAutor = Autor.objects.all()
    novoAutor.nome("Autor 2", "Autor 3")
    novoAutor.telefone(47984211417, 47,988786826)
    novoAutor.save()
    return HttpResponse("")
    
def inserirEditora(request):
    novaEditora = Editora.objects.all()
    novaEditora.descricao("Editora 1")
    novaEditora.telefone(47999256428)
    novaEditora.save()
    return HttpResponse("")

def inserirLivro(request):
    novoLivro = Livro.objects.all()
    novoLivro.Titulo('Django Framework')
    novoLivro.paginas(100)
    novoLivro.isbn(220010)
    novoLivro.Autores('Autor 2')
    novoLivro.editora('Editora 1')
    novoLivro.save()
    
    return HttpResponse("")

