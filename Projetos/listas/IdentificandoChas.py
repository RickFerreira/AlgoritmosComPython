resposta = int(input())
lista = []
lista = input().split(" ")#ler todos os valores na mesma linha e já adiciona na lista
inteiro = []
cont = 0

for i in lista:
    inteiro.append(int(i)) #faz uma lista de valores inteiros, com todos os valores de string da outra lista

for j in range(5):
    if inteiro[j] == resposta: #percorre a lista e compara cada valor com a resposta certa
        cont += 1
print(cont)
