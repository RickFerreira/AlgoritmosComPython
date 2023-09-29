nota1 = float(input("Digite a primeira média: "))
nota2 = float(input("Digite a segunda média: "))
nota3 = float(input("Digite a terceira média: "))

lista = [nota1, nota2, nota3]
media = sum(lista) / len(lista)

print("Média Semestral: {:.2f}".format(media))

if media >= 7.0:
    print("Aluno aprovado.")
elif media >= 4.0:
    print("Aluno deve fazer prova final.")
else:
    print("Aluno reprovado.")
