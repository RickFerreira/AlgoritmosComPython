maior = 0
lista = []
while True: #enquanto na frase não for digitado 0 continua perguntando frases
    frase = input()
    if frase == '0':
        break
    else:
        frases = frase.split() #pega a frase e faz uma lista com cada palavra e adiciona em frases
        for j in frases:
            lista.append(j) #para cada frase pega todos os itens e adiciona na lista, criando uma lista com todas as frases
        for i in range(len(frases)): #para cada palavra eu faço um print do seu tamanho e um - para o proximo
            if i < len(frases)-1:
                print(len(frases[i]), end="-")
            else:
                print(len(frases[i]))
        for k in lista: #pego a lista com todos os itens de todas as listas e percorro pra descbrir o item com mais caracteres
            if len(k) >= maior:
                maior = len(k)
                nome = k
print('Maior palavra: {}'.format(nome))
