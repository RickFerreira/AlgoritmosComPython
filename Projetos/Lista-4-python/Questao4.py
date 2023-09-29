valor = int(input("Digite o valor a ser sacado: "))

cedulas_50 = valor // 50
valor %= 50

cedulas_10 = valor // 10
valor %= 10

if valor != 0:
    print("Não é possível sacar o valor exato com as cédulas disponíveis.")

print("Foi sacado: ")

if cedulas_50 > 0:
    print('{} Cédulas de 50'.format(cedulas_50))
if cedulas_10 > 0:
    print('{} Cédulas de 10'.format(cedulas_10))
