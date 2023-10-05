count = 0
soma = 0

for i in range(6):
    valor = float(input())

    if valor > 0:
        count += 1
        soma += valor

print("{} valores positivos".format(count))
print("{:.1f}".format(soma/count))