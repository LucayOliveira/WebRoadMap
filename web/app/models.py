from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):
  nome = models.CharField(max_length=200, null=True, blank=True)
  email = models.CharField(max_length=200, null=True, blank=True)
  telefone = models.CharField(max_length=200, null=True, blank=True)
  id_sessao = models.CharField(max_length=200, null=True, blank=True)
  usuario = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)

class Categoria(models.Model):
  nome = models.CharField(max_length=200, null=True, blank=True)

class Tipo(models.Model):
  nome = models.CharField(max_length=200, null=True, blank=True)

class Produto(models.Model):
  imagem = models.CharField(max_length=400, null=True, blank=True)
  nome = models.CharField(max_length=200, null=True, blank=True)
  preco = models.DecimalField(max_digits=10, decimal_places=2)
  ativo = models.BooleanField(default=True)
  categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.SET_NULL)
  tipo = models.ForeignKey(Tipo, null=True, blank=True, on_delete=models.SET_NULL)

class ItemEstoque(models.Model):
  cor = models.CharField(max_length=200, null=True, blank=True)
  tamanho = models.CharField(max_length=200, null=True, blank=True)
  quantidade = models.IntegerField(default=0)
  Produto = models.ForeignKey(Produto, null=True, blank=True, on_delete=models.SET_NULL)

class Endereco(models.Model):
  rua = models.CharField(max_length=400, null=True, blank=True)
  numero = models.IntegerField(default=0)
  complemento = models.CharField(max_length=200, null=True, blank=True)
  cep = models.CharField(max_length=200, null=True, blank=True)
  cidade = models.CharField(max_length=200, null=True, blank=True)
  estado = models.CharField(max_length=200, null=True, blank=True)
  cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.SET_NULL)

class Pedido(models.Model):
  finalizado = models.BooleanField(default=False)
  codigo_transacao = models.CharField(max_length=200, null=True, blank=True)
  data_finalizacao = models.DateTimeField(null=True, blank=True)
  endereco = models.ForeignKey(Endereco, null=True, blank=True, on_delete=models.SET_NULL)
  cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.SET_NULL)

class ItensPedido(models.Model):
  quantidade = models.IntegerField(default=0)
  pedido = models.ForeignKey(Pedido, null=True, blank=True, on_delete=models.SET_NULL)
  item_estoque = models.ForeignKey(ItemEstoque, null=True, blank=True, on_delete=models.SET_NULL)

    