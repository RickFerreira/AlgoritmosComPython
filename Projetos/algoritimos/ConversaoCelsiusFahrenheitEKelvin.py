escala = input()
temperatura = float(input())

if escala == 'C':
    if temperatura < -273.0:
        print('Valor de temperatura abaixo do minimo')
    else:
        print('{:.2f} F'.format((temperatura * 9/5) + 32))
        print('{:.2f} K'.format(temperatura + 273.15))

elif escala == 'F':
    if temperatura < -459.67:
        print('Valor de temperatura abaixo do minimo')
    else:
        print('{:.2f} C'.format((temperatura - 32) * 5/9))
        print('{:.2f} K'.format((temperatura - 32) * 5/9 + 273.15))

elif escala == 'K':
    if temperatura < 0.0:
        print('Valor de temperatura abaixo do minimo')
    else:
        print('{:.2f} C'.format(temperatura - 273.15))
        print('{:.2f} F'.format((temperatura - 273.15) * 9/5 + 32))
