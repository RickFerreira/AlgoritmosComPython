dia = input()
preco = float(input())
produto = input()
nome = input()

if dia == 'seg' or dia == 'ter' or dia == 'qua':
    if produto == 'ouro':
        valor = preco / 2
        print('O preco do produto {} no dia {} eh {:.2f}'.format(nome,dia,valor))
    else:
        valor = preco * 2
        print('O preco do produto {} no dia {} eh {:.2f}'.format(nome, dia, valor))

elif dia == 'qui' or dia == 'sex':
    if 10.00<=preco<=100.00:
        valor = preco / 3
        print('O preco do produto {} no dia {} eh {:.2f}'.format(nome,dia,valor))
    else:
        valor = preco * 2
        print('O preco do produto {} no dia {} eh {:.2f}'.format(nome, dia, valor))

elif dia == 'sab':
    if produto == 'prata':
        valor = preco*3
        print('O preco do produto {} no dia {} eh {:.2f}'.format(nome,dia,valor))
    else:
        valor = preco * 2
        print('O preco do produto {} no dia {} eh {:.2f}'.format(nome, dia, valor))

else:
    valor = preco*2
    print('O preco do produto {} no dia {} eh {:.2f}'.format(nome,dia,valor))
