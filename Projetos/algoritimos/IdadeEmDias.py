N = int(input())
anos = 0
meses = 0

while (N>=365):
    anos+=1
    N-=365
while (N>=30):
    meses+=1
    N-=30
dias = N

print('{} ano(s)'.format(anos))
print('{} mes(es)'.format(meses))
print('{} dia(s)'.format(dias))
