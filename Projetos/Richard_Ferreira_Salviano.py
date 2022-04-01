a = "COBOL"
indice = 0
while True:
    palavra = input().upper().split("-")
    if palavra[0] == "FIM":
        break
    cont = 0
    for i in palavra:
        if i[0] == a[indice]:
            cont += 1
        elif i[-1] == a[indice]:
            cont += 1
        indice += 1
        if indice == 5:
            indice = 0
    if cont == 5:
        print("GRACE HOPPER")
    else:
        print("BUG")