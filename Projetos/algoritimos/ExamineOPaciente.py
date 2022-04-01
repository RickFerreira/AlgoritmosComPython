temperatura = float(input())
problemas = input()

if problemas == 'S' or problemas == 'N':

    if temperatura >= 37 and problemas == 'S':
        print('Exames Especiais')

    elif temperatura >= 37 and problemas == 'N':
        print('Exames Basicos')

    elif temperatura < 37 and problemas == 'S':
        print('Exames Basicos')

    elif temperatura < 37 and problemas == 'N':
        print('Liberado')

    elif temperatura < 37 and problemas == 'N':
        print('Liberado')
else:
    print('Erro')
