"""
nome = input('Entre com seu nome: ')
print(f'ola {nome}, você está logado!')
"""


def somar1():
    x = float(input('Entre com o primeiro número: '))
    y = float(input('Entre com o segundo número: '))
    soma = x + y
    print(soma)


def somar2(a, b):
    soma = a + b
    print(soma)


def somar3(a, b):
    return a + b


x = float(input('Entre com o primeiro número: '))
y = float(input('Entre com o segundo número: '))

# somar1()
# somar2(x, y)
resultado = somar3(x, y)
print(resultado)
print(resultado)

