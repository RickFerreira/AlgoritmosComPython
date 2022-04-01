n = int(input())
lista = []
lista = input().split(" ")

while len(lista) > n:
    lista.pop()

verificar = lista[1]
cont = 0
maior = 0

for i in lista:
    if i == verificar:
        cont += 1
    else:
        if cont > maior:
            maior = cont
        cont = 0
    verificar = i

print(maior)


