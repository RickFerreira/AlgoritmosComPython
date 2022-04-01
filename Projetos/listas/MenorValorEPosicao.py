n = int(input())
lista = input().split(" ")
menor = 0
posicao = 0

for i in range(n):
    valor = int(lista[i])
    if valor < menor:
        menor = valor
        posicao = i

print('Menor valor: {}'.format(menor))
print('Posicao: {}'.format(posicao))
