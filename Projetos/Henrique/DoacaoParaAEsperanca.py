agora = 0
futuro = 0
while True:
    valor = int(input())
    if valor >= 1:

        opcao = int(input())

        while opcao > 2 or opcao < 0:
            print('Valor invalido')
            opcao = int(input())

        if opcao == 1:
            agora += valor
        elif opcao == 2:
            agora += valor

            meses = int(input())

            while meses > 12 or meses < 2:
                print('Favor digitar valor entre 2 e 12, inclusive')

                meses = int(input())
            if 2 <= meses <= 12:
                futuro += valor*meses-valor

    else:
        break

print('Total arrecadado para agora: R$ {:.2f}'.format(agora))
print('Total arrecadado para meses futuros: R$ {:.2f}'.format(futuro))
