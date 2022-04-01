n = int(input())

for x in range(10000000000000):
    if n != -1:
        tot = 1
        for y in range(1, n+1):
            tot = tot*y
            y += 1
        print(tot)
        n = int(input())
    else:
        break

