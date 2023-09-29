peso = float(input("Digite o peso (em kg): "))
altura = float(input("Digite a altura (em metros): "))

imc = peso / (altura ** 2)

if imc < 20:
    faixaDeRisco = "Abaixo do peso"
elif 20 <= imc < 25:
    faixaDeRisco = "Normal"
elif 25 <= imc < 30:
    faixaDeRisco = "Excesso de peso"
elif 30 <= imc < 35:
    faixaDeRisco = "Obesidade"
else:
    faixaDeRisco = "Obesidade mórbida"

print('O IMC é: {:.2f}'.format(imc))
print('Faixa de risco: {}'.format(faixaDeRisco))
