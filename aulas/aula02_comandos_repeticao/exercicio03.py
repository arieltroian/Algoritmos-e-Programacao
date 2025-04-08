''' Exercício 3: use o comando while em conjunto com o comando if para imprimir todos os 
números múltiplos de 4 do 1 ao 100. '''

i = 1
while i <= 100:
    if i % 4 == 0:
        print(i)
    i = i + 1
