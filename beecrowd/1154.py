id = int(input())

soma = 0
cont = 0

while id > 0:

    soma += id
    cont+=1

    id = int(input())


print(f"{soma/cont:.2f}")