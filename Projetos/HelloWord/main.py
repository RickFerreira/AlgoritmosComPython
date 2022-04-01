soma = 0
def fatorial(x):
    fat = 1
    i = 2
    while i <= x:
        fat = fat*i
        i = i + 1
    return fat
def s(y):
    S = 0
    for j in range(y+1):
        S += y/y(j)
    return S
def verificar(z):
    if (z % 3) == 0:
        return True
    else:
        return False
for i in range(5):
    valor = int(input())
    if verificar(valor) == True:
        soma += fatorial(valor)
    else:
        soma += s(valor)
print('{:.2f}'.format(soma))