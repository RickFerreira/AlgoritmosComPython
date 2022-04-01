lista = [] #declarando uma lista para a soma
numeros = [] #declarando uma lista para os numeros
for i in range(5):
    numero = int(input())
    soma = 0
    numeros.append(numero) #adicionando na lista os valores que o usuario digitar
    for j in range(1, numero+1):
        if (numero % j) == 0:
            soma += j
    lista.append(soma) #adicionando todos os valores de soma na lista

total = max(lista) #pegando o valor maximo de uma lista
indice = lista.index(total) #descobrindo onde se encontra esse valor na lista

print('{}'.format(numeros[indice]))  #imprimindo o numero que esta na posicao encontrada, so que da lista de numeros