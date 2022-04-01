a = int(input()) #ler a variavel

for i in range(1, a+1): #faz um for que inicia de 1 e vai atpe o número digitado mais um
    for j in range(i): #vou fazendo o for rodar de 0(j) até chegar chegar no i imprimindo o i, i vezes na mesma linha
        print(i, end = "") #essa função end faz ir imprimindo o número na mesma linha
    print() #pulando uma linha
'''
por exemplo, se o valor informado for 2 ele inicia o i em 1 entra no j e e vai repeti uma vez, 
imprimindo o i na mesma linha uma vez, depois ele adiciona 1 no primeiro for e agora i é 2
o j se repete duas vezes, imprimindo o valor de i na mesma linha duas vezes.
'''
