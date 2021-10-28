from random import randint

vetor = []
par = []
impar = []

for c in range(0, 20):
    numero = randint(1, 100)
    vetor.append(numero)
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print(f"Vetor Original: {vetor} "
      f"\nVetor Par:      {par}"
      f"\nVetor Impar:    {impar}")
