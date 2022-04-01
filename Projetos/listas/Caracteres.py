while True:
    n = int(input())
    if n == 0:
        break
    else:
        frase = input()
        a  = frase[0:n:1]
        print(a[::-1])
