''' Exercício 4: Faça um programa que funcione como uma calculadora simples. Leia dois valores 
numéricos e a operação aritmética a ser executada (+, -, / ou *), calcule e exiba o resultado
da referida operação.
O programa deve avisar o usuário se foi digitada uma operação inválida. '''

num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))
operacao = str(
    input("Escolha uma das seguintes operações aritméticas: (+, -, / ou *) "))

if operacao == "+":
    soma = num1 + num2
    print(f"O resultado da soma é {soma}")

elif operacao == "-":
    subtracao = num1 - num2
    print(f"O resultado da subtração é {subtracao}")

elif operacao == "/":
    divisao = num1 / num2
    print(f"O resultado da divisão é {divisao}")

elif operacao == "*":
    multiplicacao = num1 * num2
    print(f"O resultado da multiplicação é {multiplicacao}")

else:
    print("Digite uma operação válida!")
