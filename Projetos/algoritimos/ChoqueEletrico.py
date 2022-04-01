level = int(input())

if 1<=level<=20:
    print('Potencia de : {} W'.format(20 + level**3))
elif 21<=level<=40:
    print('Potencia de : {} W'.format(8000 + (level-10)**2))
elif 41<=level<=60:
    print('Potencia de : {} W'.format(9000 + 5*level))
elif 61<=level<=80:
    print('Potencia de : {} W'.format(9300 + 2*level))
elif 81<=level<=100:
    print('Potencia de : {} W'.format(9500 + level))
