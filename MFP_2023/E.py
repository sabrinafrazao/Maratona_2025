bits = list(map(int, input().split()))

msg = bits[:7]
seg = bits[7]

cont_one = sum(msg)

if (cont_one % 2 == 0 and seg != 0) or (cont_one % 2 == 1 and seg != 1):
    print("S")
else:
    print("N?")