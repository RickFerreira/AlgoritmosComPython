contador = 0
while True:
    portugues = int(input())
    if portugues < 0:
        break
    else:
        matematica = int(input())
        redacao = float(input())
        if portugues >= 40:
            if matematica >= 21:
                if redacao >= 7:
                    contador += 1
print(contador)
