f, c = input().split(" ")
f = int(f)
c = int(c)
fileiras = []
cont = cont2 = menor = maior = 0
for i in range(f):
    colunas = []
    for j in range(c):
        entrada = int(input())
        colunas.append(entrada)
        if entrada < 0:
            menor += 1
        if entrada > 0:
            maior += 1
        if i == j:
            cont += entrada
        if i+j == f-1:
            cont2 += entrada
    fileiras.append(colunas)
print('Matriz formada:')
for k in fileiras:
    for l in range(c):
        if l == c-1:
            print(k[l])
        else:
            print(k[l], end=" ")
if f == c:
    print('A diagonal principal e secundaria tem valor(es) {} e {} respectivamente.'.format(cont, cont2))
else:
    print('A diagonal principal e secundaria nao pode ser obtida.')
print('A matriz possui {} numero(s) menor(es) que zero.'.format(menor))
print('A matriz possui {} numero(s) maior(es) que zero.'.format(maior))