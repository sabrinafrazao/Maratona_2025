import math

n = int(input())

# fatorial = math.factorial(n)

# print(fatorial)

f = 1

for i in range(1, n+1):

    f *= i

print(f)