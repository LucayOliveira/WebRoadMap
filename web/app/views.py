from django.shortcuts import render

# Create your views here.
def homepage(request):
  return render(request,  'index.html')

def loja(request):
  return render(request,  'loja.html')

def minhaconta(request):
  return render(request,  'minhaconta.html')

def login(request):
  return render(request,  'login.html')

def carrinho(request):
  return render(request,  'carrinho.html')

def checkout(request):
  return render(request,  'checout.html')