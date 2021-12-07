from django import forms
from .models import Pedido


class FormCriarPedido(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['nome', 'email', 'logradouro', 'numero', 'complemento',
                  'bairro', 'cidade', 'uf', 'cep']
