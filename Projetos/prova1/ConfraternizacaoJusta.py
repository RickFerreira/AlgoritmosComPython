total = float(input())
N = int(input())
cont = 0
dinheiro = 0
for i in range(N):
    nome = input()
    valor = float(input())
    if valor > dinheiro:
        maior = nome
        dinheiro = valor

    cont += valor
if cont > total:
    print('{} pagou R$ {:.1f}'.format(maior, dinheiro))
    print('Valor excedente: sobra R$ {}'.format(cont - total))
else:
    print('{} pagou R$ {:.1f}'.format(maior, dinheiro))
    print('Valor insuficiente: falta R$ {}'.format(total - cont))
