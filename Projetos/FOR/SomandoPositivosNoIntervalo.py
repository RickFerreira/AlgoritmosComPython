n1 = int(input())
n2 = int(input())
somador = 0
#primeiro vou ver qual o número maior, pra poder ir do menor para o maior
if n1 < n2:
    maior = n2
    menor = n1

else:
    maior = n1
    menor = n2

for i in range(menor, maior+1):
#para cada indice do número menor até o maior ele verifica se é positivo, caso seja soma esse indice no somador
    if i > 0:
        somador += i

    menor += 1

print(somador)
