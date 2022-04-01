N = int(input())
horas = 0
minutos = 0
segundos = 0
while (N>=3600):
    horas+=1
    N-=3600
while (N>=60):
    minutos+=1
    N-=60
segundos = N

print('{}:{}:{}'.format(horas,minutos,segundos))

