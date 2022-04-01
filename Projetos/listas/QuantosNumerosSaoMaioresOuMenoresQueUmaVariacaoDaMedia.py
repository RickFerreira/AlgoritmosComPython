n = int(input())
lista = []
for i in range(n):
    notas = float(input())
    lista.append(notas)

soma = sum(lista) #soma todos os valores da lista
media = soma/n
maior = [x for x in lista if x > (media*1.1)] #faz uma lista com todos os valores maiores que 7.7
menor = [x for x in lista if x < (media*0.9)] #faz uma lista com todos os valores menores que 6.3

print('{:.2f}'.format(media))
print(len(maior))
print(len(menor))
