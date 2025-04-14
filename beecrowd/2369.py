
n = int(input())

valor = 7

# 11 a 30

if n > 10:
    if n <= 30:

        valor = valor + (n - 10) * 1

    else:

        valor = valor + (20*1)  


# 31 a 100

if n > 30:

    if n <= 100:

        valor = valor + (n - 30) * 2

    else:
        valor = valor + (70*2)

# acima de 100

if n > 100:

    valor = valor + (n - 100) * 5

print(valor)