N1,N2,N3,N4 = (input().split(" "))
N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
N4 = float(N4)

media = (((N1*2)+(N2*3)+(N3*4)+(N4*1))/10)

print('Media: {:.1f}'.format(media))

if media>=7.0:
    print('Aluno aprovado.')
    
elif media<5.0:
    print('Aluno reprovado.')
    
elif 5.0<=media<6.9:
    
    print('Aluno em exame.')
    exame = float(input())
    print('Nota do exame: {:.1f}'.format(exame))
    media2 = ((exame+media)/2)

    if media2>=5.0:
        print('Aluno aprovado.')
        
    elif media2<=4.9:
        print('Aluno reprovado.')

    print('Media final: {:.1f}'.format(media2))
