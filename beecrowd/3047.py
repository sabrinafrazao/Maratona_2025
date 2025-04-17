m = int(input())
a = int(input())
b = int(input())


# m = a + b + c -> como chegar no calculo do terceiro filho, substituir os valores na forma e usar os conhecimentos basicos de matematica

# Calcula o valor do terceiro filho
c = m - a - b

# Verifica qual filho é o mais velho
if a > b and a > c:
    # Se 'a' é maior que 'b' e 'c', então 'a' é o filho mais velho
    filho_velho = a

elif b > a and b > c:
    # Se 'b' é maior que 'a' e 'c', então 'b' é o filho mais velho
    filho_velho = b

else:
    # Caso contrário, 'c' é o filho mais velho
    filho_velho = c
    

# Imprime o valor do filho mais velho
print(filho_velho)




# outra forma de fazer, usando a função max()
# m = int(input())
# a = int(input())
# b = int(input())

# c = m - a - b
# filho_velho = max(a,b,c)