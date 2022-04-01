inicial = float(input())
total = inicial
meta = 0

for i in range(6):
    dia = float(input())
    total += dia

    if (dia-inicial) >= 0.50:
        meta += 1
    inicial = dia

print('R$ {:.2f}'.format(total))
print(meta)
