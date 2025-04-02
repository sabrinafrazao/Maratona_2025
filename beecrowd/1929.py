# Dados os comprimentos de quatro varetas
# Comprimento das varetas
# selecionar três varetas, dentre as quatro, e formar um triângulo.

# Entrada de valores dos comprimentos das varetas
A, B, C, D = map(int, input().split())


# Verificando todas as combinações possíveis de três varetas
if (A + B > C and A + C > B and B + C > A) or \
    (A + B > D and A + D > B and B + D > A) or \
    (A + C > D and A + D > C and C + D > A) or \
    (B + C > D and B + D > C and C + D > B):

    print("S")

else:

    print("N")









