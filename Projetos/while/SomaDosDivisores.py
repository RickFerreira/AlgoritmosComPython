contador = 0
for i in range(5):
    numero = int(input())
    soma = 0

    for j in range(1, numero+1):
        if (numero % j) == 0:
            soma += j

    if soma > contador:
        contador = soma
        final = numero

print('{}'.format(final))
