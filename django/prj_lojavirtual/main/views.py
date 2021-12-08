from django.shortcuts import render
from .forms import ContatoForm
from django.contrib import messages


def index(request):
    return render(request, 'main/index.html')


def sobre(request):
    return render(request, 'main/sobre.html')


def contato(request):

    form = ContatoForm(request.POST or None)
    print(f'Post: {request.POST}')

    if str(request.method) == 'POST':
        if form.is_valid():

            form.send_mail()

            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            messages.success(request, 'E-mail enviado com sucesso!')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar o e-mail')

    context = {
        'form': form
    }
    return render(request, 'main/contato.html', context)

