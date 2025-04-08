''' Exercício 1: usando os comandos condicionais solicite para o usuário o ano, 
mês e dia de seu nascimento (use três variáveis para armazenar os valores) e, 
usando os comandos condicionais, calcule e imprima a sua idade em anos. '''

dia = input("Dia do nascimento: ")
mes = input("Mês do nascimento: ")
ano = input("Ano do nascimento: ")

idade = 2025 - int(ano)

if int(mes) > 3:
    print(idade - 1)

else:
    if int(dia > 25):
        print(idade - 1)

    else:
        print(idade)
