quantidade_pessoas = int(input("Digite a quantidade de pessoas que deseja ler a idade: "))


def contador(repeticoes):
    idade_total = 0
    for c in range(1, quantidade_pessoas+1):
        idade = int(input(f"{c}. Digite a idade: "))
        idade_total += idade
    return idade_total

def mediaTurma(idade_total, quantidade_pessoas):
    media = idade_total / quantidade_pessoas
    if media <= 25:
        status = "Jovem"
    elif media <= 60:
        status = "Adulta"
    else:
        status = "Idosa"
    return status


print(f"Sua turma é uma turma: {mediaTurma(contador(quantidade_pessoas), quantidade_pessoas)}")
