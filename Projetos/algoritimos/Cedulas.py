N = float(input())
G = N

cem = int(0)
cinquenta = int(0)
vinte = int(0)
dez = int(0)
cinco = int(0)
dois = int(0)
um = int(0)

while (N>=100):
    cem+=1
    N-=100
while (N>=50):
    cinquenta+=1
    N-=50
while (N>=20):
    vinte+=1
    N-=20
while (N>=10):
    dez+=1
    N-=10
while (N>=5):
    cinco+=1
    N-=5
while (N>=2):
    dois+=1
    N-=2
while (N>=1):
    um+=1
    N-=1

print(int(G))
print('{} nota(s) de R$ 100,00'.format(int(cem)))
print('{} nota(s) de R$ 50,00'.format(int(cinquenta)))
print('{} nota(s) de R$ 20,00'.format(int(vinte)))
print('{} nota(s) de R$ 10,00'.format(int(dez)))
print('{} nota(s) de R$ 5,00'.format(int(cinco)))
print('{} nota(s) de R$ 2,00'.format(int(dois)))
print('{} nota(s) de R$ 1,00'.format(int(um)))
