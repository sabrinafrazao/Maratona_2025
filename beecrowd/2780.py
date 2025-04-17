d = int(input())

# Verifica em qual faixa de distância 'd' se encontra e atribui o valor correspondente a 'p' que seria a quantidade de pontos
if d <= 800:
    # Se 'd' é menor ou igual a 800, 'p' é 1
    p = 1

elif d > 800 and d <= 1400:
    # Se 'd' está entre 801 e 1400, 'p' é 2
    p = 2

elif d > 1400 and d <= 2000:
    # Se 'd' está entre 1401 e 2000, 'p' é 3
    p = 3


print(p)