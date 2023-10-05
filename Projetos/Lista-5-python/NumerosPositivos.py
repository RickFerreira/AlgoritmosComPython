a = 0
for i in range(6):
    valor = float(input())
    i+=1
    if valor > 0:
        a += 1
print("{} valores positivos".format(a))