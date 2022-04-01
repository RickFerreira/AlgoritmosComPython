n = int(input())
lista = []
cont = 0.0
if n == 0:
    print('Numero de notas invalido.')
else:
    for i in range(n):
        notas = float(input())
        cont += notas
        lista.append(notas)
        posicao = lista.index(notas)
        print('Nota {}: {}'.format(posicao+1, notas))
    print('Media: {:.2f}'.format(cont/n))
