quantidade = int(input())
cidade = input()
quartos = int(input())
if cidade.lower() == 'pipa':

    if quartos == 2:
        valor = (600+(75*quantidade))

    elif quartos == 3:
        valor = (900+(75*quantidade))


else:

    if quartos == 3:
        valor = (950+(60*quantidade))

    else:
        valor = (1120+(60*quantidade))

print('{:.2f}'.format(valor))
print('{:.2f}'.format(valor/quantidade))
