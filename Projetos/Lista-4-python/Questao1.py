numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

if numero1 >= numero2 >= numero3:
    maior = numero1
elif numero2 >= numero3:
    maior = numero2
else:
    maior = numero3
  
print('O maior número é o {}'.format(maior))