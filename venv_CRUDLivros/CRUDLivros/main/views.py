from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView
from django.http import HttpResponse
from django.contrib import auth, messages
# from main import urls
from main.models import Livro
import datetime

# Create your views here.

def index(request):
    return HttpResponse("Você está na página index de livros")

def livro_list(request):
    lista_livros = Livro.objects.all()
    for livro in lista_livros:
        print(livro)
    return render(request, 'livros/livro_list.html', {'lista' : lista_livros})

def inserir(request):
    novoLivro = Livro()
    novoLivro.Titulo('Django Framework')
    novoLivro.paginas(100)
    novoLivro.isbn(220010)
    novoLivro.Autores('Autor 2')
    novoLivro.editora('Editora 1')
    
    return HttpResponse("")

