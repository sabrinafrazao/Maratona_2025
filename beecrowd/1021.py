n = float(input())

centavos = int(round(n * 100))

notas =  [ 10000, 5000, 2000, 1000, 500, 200]

moedas = [100, 50, 25, 10, 5, 1]



print("NOTAS:")

for nota in notas:

    qtd_notas = centavos // nota


    print(f"{qtd_notas} nota(s) de R$ {nota/100:.2f}")

    centavos %= nota



print("MOEDAS:")

for moeda in moedas:

    qtd_moeda = centavos // moeda

    print(f"{qtd_moeda} moeda(s) de R$ {moeda/100:.2f}")

    centavos %= moeda
