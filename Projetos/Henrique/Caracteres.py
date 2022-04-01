while True:
    n = int(input())
    f = str(input())
    if n != 0:
        print(f[n-1::-1])
    else:
        break
