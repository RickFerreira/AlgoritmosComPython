PSNR = int(input())
enquadramento = input()
exposicao = input()

if 80<=PSNR<=90:
    if enquadramento == 'bom' or enquadramento == 'excelente':

        if exposicao == 'bem exposta':
            print('para imprimir')
        elif exposicao == 'subexposta' or exposicao == 'superexposta':
            print('boa')
        else:
            print('marromeno')
    else:
        print('marromeno')

elif 50<=PSNR<=80:
    if enquadramento == 'excelente':

        if exposicao == 'bem exposta':
            print('boa')

        else:
            print('marromeno')

    else:
        print('marromeno')

elif PSNR<50:
    if enquadramento == 'excelente':

        if exposicao == 'bem exposta':
            print('marromeno')

        else:
            print('lixo')

    else:
        print('lixo')
