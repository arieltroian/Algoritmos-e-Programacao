''' Exercício 10: escreva um programa para ler N números inteiros digitados pelo usuário e contar quantos 
destes valores são negativos. Apresentar esta informação ao final do programa. '''

negativo = 0
nvalores = int(input("Quantos números serão digitados? "))
for i in range(nvalores):
    num = int(
        input(f"Digite um número positivo ou negativo {i + 1}/{nvalores}: "))
    if num < 0:
        negativo += 1
print(f"Foram digitados {negativo} números negativos")
