N = float(input())
cem = int(0)
cinquenta = int(0)
vinte = int(0)
dez = int(0)
cinco = int(0)
dois = int(0)

um = int(0)
cinquent = int(0)
vint = int(0)
cinc = int(0)
de = int(0)
u = int(0)


while (N>100-0.00001):
    cem+=1
    N-=100
while (N>50-0.00001):
    cinquenta+=1
    N-=50
while (N>20-0.00001):
    vinte+=1
    N-=20
while (N>10-0.00001):
    dez+=1
    N-=10
while (N>5-0.00001):
    cinco+=1
    N-=5
while (N>2-0.00001):
    dois+=1
    N-=2
while (N>1-0.00001):
    um+=1
    N-=1
while (N>0.50-0.00001):
    cinquent+=1
    N-=0.50
while (N>0.25-0.00001):
    vint+=1
    N-=0.25
while (N>0.10-0.00001):
    de+=1
    N-=0.10
while (N>0.05-0.00001):
    cinc+=1
    N-=0.05
while (N>0.01-0.00001):
    u+=1
    N-=0.01

print("NOTAS:")
print('{} nota(s) de R$ 100.00'.format(int(cem)))
print('{} nota(s) de R$ 50.00'.format(int(cinquenta)))
print('{} nota(s) de R$ 20.00'.format(int(vinte)))
print('{} nota(s) de R$ 10.00'.format(int(dez)))
print('{} nota(s) de R$ 5.00'.format(int(cinco)))
print('{} nota(s) de R$ 2.00'.format(int(dois)))
print("MOEDAS:")
print('{} moeda(s) de R$ 1.00'.format(int(um)))
print('{} moeda(s) de R$ 0.50'.format(int(cinquent)))
print('{} moeda(s) de R$ 0.25'.format(int(vint)))
print('{} moeda(s) de R$ 0.10'.format(int(de)))
print('{} moeda(s) de R$ 0.05'.format(int(cinc)))
print('{} moeda(s) de R$ 0.01'.format(int(u)))
