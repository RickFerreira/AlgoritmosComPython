total = 0
for i in range(7):
    qnt = int(input())
    tamanho = input()
    if tamanho == 'G' or tamanho == 'g':
        a = 16 * qnt
        total += a
    else:
        a = 10 * qnt
        total += a

print(total)
print(int(total*2/7))
