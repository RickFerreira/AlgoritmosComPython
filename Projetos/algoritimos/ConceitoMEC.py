livros = int(input())
alunos = int(input())
total = alunos/livros

if total <= 8:
    print('A')
elif 9<=total<=12:
    print('B')
elif 13<=total<=18:
    print('C')
else:
    print('D')
