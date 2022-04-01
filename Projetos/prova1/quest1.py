U = int(input())

if U <= 99:
    valor = U*1.35
    if valor <= 35:
        print('35.00')
        print('1.35')
    else:
        print('{:.2f}'.format(valor))
        print('1.35')

elif 100 <= U <= 299:
    valor = U*1.55
    print('{:.2f}'.format(valor))
    print('1.55')

elif 300 <= U <= 574:
    if U > 300:
        valor = U*1.75*1.1
    else:
        valor = U*1.75
    print('{:.2f}'.format(valor))
    print('1.75')

else:
    valor = U*2.15*1.1
    print('{:.2f}'.format(valor))
    print('2.15')
