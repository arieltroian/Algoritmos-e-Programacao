''' Exercício 3: pergunte a idade em anos do usuário e o classifique quanto a 
sua categoria etária (criança até 12 anos, adolescente dos 13 aos 17 anos, adulto
 dos 18 aos 64 anos ou idoso se mais de 64 anos). Se o usuário digitar um número 
 negativo ou maior que 150 anos o programa deve imprimir uma mensagem de erro. '''

idade = float(input("Qual a sua idade? "))
if idade >= 0 and idade <= 12:
    print("Criança")

elif idade >= 13 and idade <= 17:
    print("Adolescente")

elif idade >= 18 and idade <= 64:
    print("Adulto")

elif idade >= 65 and idade <= 149:
    print("Idoso)")

else:
    print("Digite uma idade válida!")
