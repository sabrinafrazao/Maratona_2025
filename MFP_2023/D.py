m1, m2 = map(float, input().split())

x1, x2 = map(float, input().split())

f = float(input())


d = x2 - x1


G = ((d*d) * f)/(m1*m2)

print(round(G,10))