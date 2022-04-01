glicose = int(input())
total = 0
contador = 0
while glicose != 0:
    total += glicose
    contador += 1
    glicose = int(input())

media = total/contador

if media < 110:
    print('Glicose Normal')
elif media >= 200:
    print('Glicose Muito Alta')
else:
    print('Glicose Alterada')
