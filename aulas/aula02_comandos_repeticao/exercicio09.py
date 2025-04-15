''' Exercício 9: escreva um programa para ler 10 números inteiros digitados pelo usuário e contar quantos 
destes valores são negativos. Apresentar esta informação ao final do programa. '''

negativo = 0

for i in range(10):
    num = int(input(f"Digite um número positivo ou negativo {i + 1}/10: "))
    if num < 0:
        negativo += 1
print(f"Foram digitados {negativo} números negativos")
