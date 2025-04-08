''' Exercício 8: faça um programa que peça para o usuário 10 notas e imprima quantas notas são 
maiores ou iguais a 6. '''

for i in range(0, 10):
    notas = int(input("Digite a nota: "))
    if notas >= 6:
        print(notas)
