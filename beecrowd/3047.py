m = int(input())
a = int(input())
b = int(input())

# m = a + b + c

c = m - a - b

# filho_velho = max(a,b,c)

if a > b and a > c :

    filho_velho = a

elif b >a and b > c:
    filho_velho = b

else:
    filho_velho = c
    
print(filho_velho)