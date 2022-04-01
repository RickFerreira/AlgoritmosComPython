qnt = int(input())
cont = 0
if 0 < qnt <= 5:
    for i in range(1, qnt+1):
        nota = float(input())
        cont += nota
        print('Nota {}: {}'.format(i, nota))
    print('Media: {:.2f}'.format(cont/qnt))
else:
    print('Numero de notas invalido.')
