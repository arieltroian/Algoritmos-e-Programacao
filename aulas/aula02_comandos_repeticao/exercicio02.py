''' Exercício 2: faça um programa que pergunte quantos funcionários há em uma empresa. 
Depois, para cada funcionário, solicite o valor de seu salário e apresente o valor do 
salário com um aumento de 7,5%. '''

funcionarios = int(input("Quantos funcionários tem na sua empresa? "))
while funcionarios >= 1:
    salario = float(input("Qual o salário desse funcionário? "))
    aumento = salario + salario * 7.5 / 100
    print(f"O aumento no salário é de R$ {aumento:.2f}")

    funcionarios = funcionarios - 1
