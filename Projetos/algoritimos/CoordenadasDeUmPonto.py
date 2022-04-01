X,Y = (input().split(" "))
X = float(X)
Y = float(Y)

if Y>0<X:
    print('Q1')
elif Y>0>X:
    print('Q2')
elif Y<0>X:
    print('Q3')
elif Y<0<X:
    print('Q4')
elif X==Y==0:
    print('Origem')
elif X==0!=Y:
    print('Eixo Y')
elif Y==0!=X:
    print('Eixo X')
