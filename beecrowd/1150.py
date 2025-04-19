x = int(input())
z = int(input())

while True:
    z = int(input())

    if z>x:
        break


soma = 0 
cont = 0
atual = x

while soma <=z:
    soma += atual
    atual+=1
    cont+=1

print(cont)