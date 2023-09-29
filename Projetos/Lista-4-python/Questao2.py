a = float(input("Digite o valor de a: "))
if a == 0:
    print("A equação não é do segundo grau.")
else:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

    delta = b**2 - 4*a*c

    if delta < 0:
        print("A equação não possui raízes reais.")
    elif delta == 0:
        x = -b / (2*a)
        print('A equação possui uma raiz real: x = {}'.format(x))
    else:
        x1 = (-b + delta**0.5) / (2*a)
        x2 = (-b - delta**0.5) / (2*a)
        print('A equação possui duas raízes reais: \n x1 = {} \n x2 = {}'.format(x1, x2))
