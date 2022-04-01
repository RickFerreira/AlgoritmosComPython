lista = []
lista1 = []
lista2 = []

n1 = int(input())

if n1 >= 1:
    for k in range(n1):
        item1 = int(input())
        lista1.append(item1)

    n2 = int(input())
    if n2 >= 1:
        for j in range(n2):
            item2 = int(input())
            lista2.append(item2)

        lista = lista1 + lista2
        for i in range(len(lista)):
            if i == len(lista) - 1:
                print("{}".format(lista[i]))
            else:
                print("{} ".format(lista[i]), end='')

    else:
        print('Erro - A lista deve ter pelo menos 1 elemento.')

else:
    print('Erro - A lista deve ter pelo menos 1 elemento.')
