from django.urls import path
from .views import listar_produtos

app_name = 'produtos'

urlpatterns = [
    path('', listar_produtos, name='listar_produtos'),
]
