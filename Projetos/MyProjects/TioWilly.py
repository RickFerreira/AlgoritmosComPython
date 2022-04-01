a = 0
while a == 0:


    i = 0
    cnt = 0
    lista = []

    while i < 10:

        X = int(input())
        lista.append(X)

        if X == -1:
            break
        else:
            i += 1

    N = int(input())
    K = lista.count(N)
    a = lista.count(-1)


    print('{} appeared {} times'.format(N, K))

