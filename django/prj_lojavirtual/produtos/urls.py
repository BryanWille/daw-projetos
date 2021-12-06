from django.urls import path
from .views import listar_produtos, celular

app_name = 'produtos'

urlpatterns = [
    path('', listar_produtos, name='listar_produtos'),
    path('celular', celular, name='celular'),
]
