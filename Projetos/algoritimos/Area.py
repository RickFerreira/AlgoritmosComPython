# pega 3 valores na mesma linha e atribui a variáveis
A,B,C = (input().split(" "))

A = float(A)
B = float(B)
C = float(C)

TRIANGULO = ((A*C)/2)
CIRCULO = (3.14159*(C**2))
TRAPEZIO = (((A+B)*C)/2)
QUADRADO = (B**2)
RETANGULO = (A*B)

print('TRIANGULO: {:.3f}'.format(TRIANGULO))
print('CIRCULO: {:.3f}'.format(CIRCULO))
print('TRAPEZIO: {:.3f}'.format(TRAPEZIO))
print('QUADRADO: {:.3f}'.format(QUADRADO))
print('RETANGULO: {:.3f}'.format(RETANGULO))
