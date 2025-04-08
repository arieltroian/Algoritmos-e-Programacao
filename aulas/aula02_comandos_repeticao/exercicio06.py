''' Exercício 6: usando o comando for, faça um programa que pergunte quantos funcionários há 
em uma empresa. Depois, para cada funcionário, solicite o valor de seu salário e apresente o 
valor do salário com um aumento de 7,5%. '''

funcionarios = int(input("Qunatos funcionários tem na sua empresa?"))
for i in range(funcionarios):
    salario = float(input("Qual é o valor do salário?"))
    aumento = salario + salario * 7.5 / 100
    print(f"O aumento no salário é de R$ {aumento:.2f}")
