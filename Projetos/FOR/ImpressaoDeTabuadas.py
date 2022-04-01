for x in range(10000000000):
    a = int(input())
    if 1 > a or a > 9:
        print('Insira um número inicial entre 1 e 9')
    else:
        break

for y in range(1000000000000):
    b = int(input())
    if 1 > b or b > 9:
        print('Insira um número final entre 1 e 9')
    else:
        break

if a > b:
    print('Nenhuma tabuada nesse intervalo')

if 10 > a > 0 and 10 > b > 0:
    for i in range(a, b+1):
        for j in range(1, 10):
            print('{} x {} = {}'.format(i, j, i*j))
        print()
