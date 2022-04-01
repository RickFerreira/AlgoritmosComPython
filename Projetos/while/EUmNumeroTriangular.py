numero = int(input())
contador = 1

while contador * (contador+1) * (contador+2) < numero:
    contador += 1

resultado = contador * (contador+1) * (contador+2)

if resultado == numero:
    print('{} * {} * {} = {}'.format(contador, contador+1, contador+2, numero))
    print('Verdadeiro')

else:
    print('Falso')
