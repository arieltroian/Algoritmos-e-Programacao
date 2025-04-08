''' Exercício 5: A prefeitura de Chapecó abriu uma linha de crédito para os funcionários. O valor máximo da 
prestação não poderá ultrapassar 30% do salário bruto.
Fazer um algoritmo que permita entrar com o salário bruto e o valor da prestação e informar se 
o empréstimo pode ou não ser concedido. '''

salario = float(input("Qual é o seu salário? "))
prestacao = float(input("Valor da prestação que deseja: "))
max_prestacao = 0.3 * salario

if prestacao <= max_prestacao:
    print("Empréstimo concedido")

else:
    print("Empréstimo não concedido")
