from django.shortcuts import render


def listar_produtos(request):
    return render(request, 'produtos/produtos.html')

def celular(request):
    return render(request, 'produtos/celular.html')