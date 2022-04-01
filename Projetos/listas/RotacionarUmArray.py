qnt = int(input())
lista = []
for i in range(qnt):
    valores = int(input())
    lista.append(valores)

deslocamento = int(input())
rotacao = lista[deslocamento:]+lista[:deslocamento]
#imprime tudo do deslocamento pra frente e tudo do deslocamento pra traz depois.
for i in rotacao:
    print(i)
