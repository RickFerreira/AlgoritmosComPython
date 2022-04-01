# pega 3 valores na mesma linha e atribui a variáveis
codigo1,numero1,valor1 = (input().split(" "))
codigo2,numero2,valor2 = (input().split(" "))

codigo1 = int(codigo1)
numero1 = int(numero1)
valor1 = float(valor1)

codigo2 = int(codigo2)
numero2 = int(numero2)
valor2 = float(valor2)

total = ((numero1*valor1)+(numero2*valor2))
print('VALOR A PAGAR: R$ {:.2f}'.format(total))