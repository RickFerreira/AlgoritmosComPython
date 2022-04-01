dia = int(input())
estudante = int(input())
socio = int(input())


if dia == 1 or dia == 2 or dia == 3 or dia == 4:

    valor = 15.00

    if estudante == 1:
        valor = valor*0.7
        print('ESTUDANTE: R$ {:.2f}'.format(valor))
    else:

        if socio == 1:
            print('SOCIO: R$ {:.2f}'.format(valor))
        else:
            valor = valor
            print('COMUM: R$ {:.2f}'.format(valor))

else:

    valor = 30

    if estudante == 1:
        valor = valor * 0.7
        print('ESTUDANTE: R$ {:.2f}'.format(valor))
    else:

        if socio == 1:
            valor = 30.00 * 0.8
            print('SOCIO: R$ {:.2f}'.format(valor))

        else:
            print('COMUM: R$ {:.2f}'.format(valor))
