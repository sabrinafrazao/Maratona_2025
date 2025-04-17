c = int(input())

# Inicializa a variável valor, mas, poderia Inicializar com 7
valor = 0

# Verifica em qual faixa o valor de c se encontra e calcula o valor correspondente
if c <= 10:
    # Se consumo é menor ou igual a 10m³, o valor é 7
    valor = 7
    
elif c <= 30:
    # Se consumo está entre 11 e 30m³, adiciona 1 real para cada unidade acima de 10m³
    valor = 7 + (c - 10) * 1
    
elif c <= 100:
    # Se consumo está entre 31 e 100m³, adiciona 20 reais (para os primeiros 30m³) e 2 reais para cada unidade acima de 30m³
    valor = 7 + 20 + (c - 30) * 2
    
else:
    # Se consumo é maior que 100m³, adiciona 140 reais (para os primeiros 100m³) e 5 reais para cada unidade acima de 100m³
    valor = 7 + 20 + 140 + (c - 100) * 5


print(valor)
