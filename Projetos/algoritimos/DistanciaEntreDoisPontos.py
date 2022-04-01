# pega 3 valores na mesma linha e atribui a variáveis
x1,y1 = (input().split(" "))
x2,y2= (input().split(" "))

x1 = float(x1)
y1 = float(y1)

x2 = float(x2)
y2 = float(y2)

total = ((((x2-x1)**2)+(y2-y1)**2)**0.5)
print('{:.4f}'.format(total))
