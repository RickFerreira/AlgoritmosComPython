escolha = int(input('Escolha uma opção (1: Soma, 2: Subtração, 3: Multiplicação ou 4: Divisão): '))

operando1 = float(input("Digite o primeiro operando: "))
operando2 = float(input("Digite o segundo operando: "))

if escolha == 1:
    resultado = operando1 + operando2
    print('Resultado da soma = {}'.format(resultado))
elif escolha == 2:
    resultado = operando1 - operando2
    print('Resultado da subtração = {}'.format(resultado))
elif escolha == 3:
    resultado = operando1 * operando2
    print('Resultado da multiplicação = {}'.format(resultado))
else:
    if operando2 != 0:
        resultado = operando1 / operando2
        print('Resultado da divisão = {}'.format(resultado))
    else:
        print("Erro: Divisão por zero.")
