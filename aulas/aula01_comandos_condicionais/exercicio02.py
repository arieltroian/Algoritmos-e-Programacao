''' Exercício 2: use o operador ternário para identificar e imprimir se o 
número informado pelo usuário é par ou é ímpar '''

numero = int(input("Digite um número: "))

resto = numero % 2

if resto == 0:
    print("o número é par")

else:
    print("o número é ímpar")
