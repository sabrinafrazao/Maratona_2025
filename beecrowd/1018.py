
# n = int(input())

# ced_100 = n//100

# ced_50 = (n%100)//50

# ced_20 = ((n%100)%50)//20

# resto_20 = ((n%100)%50)%20

# ced_10 = resto_20//10

# ced_5 = (resto_20%10)//5

# resto_5 = ( resto_20%10)%5

# ced_2 = resto_5//2

# ced_1 = resto_5%2

# print(n)
# print(f"{ced_100} nota(s) de R$ 100,00")
# print(f"{ced_50} nota(s) de R$ 50,00")
# print(f"{ced_20} nota(s) de R$ 20,00")
# print(f"{ced_10} nota(s) de R$ 10,00")
# print(f"{ced_5} nota(s) de R$ 5,00")
# print(f"{ced_2} nota(s) de R$ 2,00")
# print(f"{ced_1} nota(s) de R$ 1,00")

n = int(input())

v_original = n

notas = [100, 50, 20, 10, 5, 2, 1]

print(v_original)

for nota in notas:

    qtd = n // nota

    print(f"{qtd} nota(s) de R$ {nota},00")

    n = n % nota