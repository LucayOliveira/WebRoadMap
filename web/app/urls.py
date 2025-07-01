from django.urls import path, include
from .views import *

urlpatterns = [
    path('', homepage, name='homepage'),
    path('loja/', loja, name='loja'),
    path('minhaconta/', minhaconta, name='minhaconta'),
    path('login/', login, name='login'),
    path('carrinho/', carrinho, name='carrinho'),
    path('checkout/', checkout, name='checkout')
]
