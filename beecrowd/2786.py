# ESCOLA QUE TROCAR DE PISOS
# COMPRARAM LAJOTAS DE 1M DE DIAGONAL
# DADO COMPRIMENTO E A LARGURA
# QUANTIDADE INTEIRAS DE LAJOTAS
# QUANTIDADE PARCIAL DE LAJOTAS

L = int(input())
C = int(input())

# Lajotas inteiras: (L * C) + ((L - 1) * (C - 1))
# Lajotas parciais: ((L - 1) * 2) + ((C - 1) * 2)

Lajotas_inteiras = (L * C) + ((L - 1) * (C - 1))

Lajotas_parciais = ((L - 1) * 2) + ((C - 1) * 2)

print(Lajotas_inteiras)
print(Lajotas_parciais)

