salario = float(input())

if salario <= 2000.00:
    var = 0
    print("Isento")
if 2000.00 < salario <= 3000.00:
    oito = salario - 2000.00
    var = oito * 0.08
if 3000.00 < salario <= 4500.00:
    varoito = 0.08 * 1000.00
    dezoito = salario - 3000.00
    var = dezoito * 0.18 + varoito
if salario > 4500.00:
    varoito = (8 / 100) * (1000.00)
    vardezoito = (18 / 100) * (1500.00)
    vinteoito = salario - 4500.00
    var = vardezoito + varoito + vinteoito * (28 / 100)
if salario > 2000.00:
    var = float(var)
    print('R$ {:.2f}'.format(var))