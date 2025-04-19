while True:

    try:
        a = list(input())

        if a[2] == "L":
            print("Esse eh o meu lugar")
        else:
            print("Oi, Leonard")

    except EOFError:
        break


