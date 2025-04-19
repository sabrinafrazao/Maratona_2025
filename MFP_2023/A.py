
t = int(input())

for i in range(t):
    n = int(input())
    p = list(map(int, input().split()))


    for j in range(n):

        atual = j

        caminho = []

        while True:
            caminho.append(atual + 1)

            atual = p[atual] - 1

            if atual == j:
                break

        print(' '.join(map(str, caminho)))