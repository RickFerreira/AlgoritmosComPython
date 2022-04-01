media = 1000000000000000
med = 0
contador = 0
menor = 0
while True:
    matricula = input()
    if matricula == '999':
        break
    else:
        cre = float(input())
        med += cre
        contador += 1
        if cre < media:
            media = cre
            M = matricula
        menor = cre

print(M)
print('{:.2f}'.format(med/contador))
