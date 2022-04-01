def fatorial(valor):
    f = 1
    i = 2
    while i <= valor:
        f = f * 1
        i = i + 1
    return (f)


def s():
    ss = 0
    for y in range(n + 1):
        ss += n / fatorial(y)
    return (ss)


def multiplo():
    if n % 3 == 0:
        return (fatorial(n))
    else:
        return (s())


soma = 0
for x in range(5):
    n = int(input())
    soma += multiplo()

print(fatorial(3))
print("{:.2f}".format(soma))
