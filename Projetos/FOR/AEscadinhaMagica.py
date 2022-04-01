a = int(input())
for i in range(a+1):
    for j in range(1, i+1):
        if j == i:
            print(j, end='')
        else:
            print(j, end=' ')
    print()
