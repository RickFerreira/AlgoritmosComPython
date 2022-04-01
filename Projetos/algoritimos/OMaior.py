A,B,C = (input().split(" "))

A = int(A)
B = int(B)
C = int(C)

MaiorAB = ((A+B+abs(A-B))/2) #formula para ver o maior
Maior = int((MaiorAB+C+abs(MaiorAB-C))/2)

print('{} eh o maior'.format(Maior))
