#Escreva um programa que receba 2 inteiro e retorne a divisão deles.

numero1 = (input("Digite o primeiro número: "))
numero1 = int(numero1)
numero2 = (input("Digite o segundo número: "))
numero2 = int(numero2)

if numero2 == 0:
  print('Não é possível fazer divisão por 0')
else:
  divisao = numero1/numero2
  print('O resultado da divisao é {}'.format(divisao))
