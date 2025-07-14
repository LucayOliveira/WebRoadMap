from django.shortcuts import render
from .models import *

# Create your views here.
def homepage(request):
  return render(request,  'index.html')

def loja(request):
  produtos = Produto.objects.all()
  context = {'produtos' : produtos}
  return render(request,  'loja.html', context)

def minhaconta(request):
  return render(request,  'minhaconta.html')

def login(request):
  return render(request,  'login.html')

def carrinho(request):
  return render(request,  'carrinho.html')

def checkout(request):
  return render(request,  'checkout.html')