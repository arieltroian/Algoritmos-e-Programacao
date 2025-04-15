''' Exercício 11: faça um algoritmo usando o comando while ou for que leia um valor inteiro fornecido pelo 
usuário e calcule a soma de seus 10 sucessores e seus 10 antecessores. A soma deve ser exibida 
ao final do programa. '''

num = int(input("Digite um número: "))
soma = 0
sub = 0
for i in range(1, 11):
    sucessores = num + i
    antecessores = num - i
    soma = soma + sucessores
    sub = sub + antecessores


print(f"{soma} e {sub}")
