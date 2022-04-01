tamanhoTeatro = 0
saldo = 0.0
cont = 0
valorEntrada = -1.0
while True:
    # Introdução
    pessoa = input('''
            ===========Bem Vindo(a)!============
            ------------------------------------
            --Você é cliente ou administrador?--
            ====================================
            -------Digite 1 para administrador--------
            ----Digite 2 para cliente-----
            ---------Digite 0 para sair---------
            ====================================
            !!!!!!! OBS. SÓ USE NÚMEROS !!!!!!!!

            Digite: ''')

    if pessoa == '0':
        print('\n' * 130)
        print('            *** Bye, até logo ***')
        break
    while True:  #enquanto não digitar um valor valido continua perguntando
        if pessoa != '1':
            if pessoa != '2':
                if pessoa != '0':

                    pessoa = input('Por favor, digite 1,2 ou 0: ')
                else:
                    break
            else:
                break
        else:
            break
    if pessoa == '0':
        print('\n' * 130)
        print('            *** Bye, até logo ***')
        break
    # Verificar se é cliente ou administrador

    # Administrador ***********************************************************
    elif pessoa == '1':
        while True:
            print('\n' * 130)
            opcaoAdm = input('''
                ========Olá administrador=========
                ==================================
                ----Qual operação deseja fazer?---
                ==================================
            -Digite 1 para selecionar o tamanho do teatro-
            ----Digite 2 para dizer o valor da entrada---- 
            =============================================
            Digite: ''')
            while True:  # enquanto não digitar um valor valido continua perguntando
                if opcaoAdm != '1':
                    if opcaoAdm != '2':

                        opcaoAdm = input('Por favor, digite 1 ou 2: ')
                    else:
                        break
                else:
                    break

            # Valor da entrada
            if opcaoAdm == '2':
                print('\n' * 130)
                valorEntrada = float(input('Qual o valor da entrada? '))
                print('''
                =============================================
                ===Valor da entrada atualizado com sucesso===
                ---------- O ingresso custa R$ {} -----------
                '''.format(valorEntrada))

                desejoEntrada = input('''
                           Deseja realizar mais alguma operação como administrador?
                           -------------------Se Sim digite 1----------------------
                           -------------------Se não digite 2----------------------
                           Digite: ''')
                while True:
                    if desejoEntrada != '1':
                        if desejoEntrada != '2':

                            desejoEntrada = input('Por favor digite 1 ou 2: ')
                        else:
                            break
                    else:
                        break

                if desejoEntrada == '2':
                    break

            # Tamanho do Teatro
            elif opcaoAdm == '1':
                print('\n' * 130)
                coluna = int(input('Quantas colunas tem o teatro? '))

                while True:  # enquanto não digitar um valor valido continua perguntando
                    if coluna < 1:
                        coluna = int(input('Por favor, digite um valor maior que 0 para a coluna: '))
                    else:
                        break

                fileira = int(input('Quantas fileiras tem o teatro? '))
                while True:  # enquanto não digitar um valor valido continua perguntando
                    if fileira < 1:
                        fileira = int(input('Por favor, digite um valor maior que 0 para a fileira: '))
                    else:
                        break

                tamanhoTeatro = coluna * fileira
                print('\n' * 130)
                print('''
                =============================================
                Tamanho do seu teatro atualizado com sucesso.
                ---------------------------------------------
                -----------O teatro tem {} lugares-----------
                ============================================='''.format(tamanhoTeatro))
                # imprimir o teatro completo
                for i in range(1, fileira + 1):
                    for j in range(1, coluna + 1):
                        print("[{}] ".format(j+cont), end=" ")
                    print()
                    cont += coluna
                cont = 0

                desejo = input('''
           Deseja realizar mais alguma operação como administrador?
           -------------------Se Sim digite 1----------------------
           -------------------Se não digite 2----------------------
           Digite: ''')
                while True:
                    if desejo != '1':
                        if desejo != '2':
                            desejo = input('Por favor digite 1 ou 2: ')
                        else:
                            break
                    else:
                        break

                if desejo == '2':
                    print('\n' * 130)
                    break

    # Cliente********************************************************************************
    elif pessoa == '2':
        while True:
            print('\n' * 130)
            opcaoCliente = input('''
                  ===============Olá!===============
                  ====Você está na aba de cliente===
                  ==================================
                  ----Qual operação deseja fazer?---
                  ==================================
              ---Digite 1 para adicionar dinheiro a conta---
              ---------Digite 2 para ver seu saldo----------
              ------Digite 3 para reservar uma cadeira------
              --------Digite 4 para pedir reembolso---------
              =============================================
              Digite: ''')
            while True:  # enquanto não digitar um valor valido continua perguntando
                if opcaoCliente != '1':
                    if opcaoCliente != '2':
                        if opcaoCliente != '3':
                            if opcaoCliente != '4':
                                if opcaoCliente != '0':
                                    opcaoCliente = input('Por favor, digite 1, 2, 3 ou 4: ')
                                else:
                                    break
                            else:
                                break
                        else:
                            break
                    else:
                        break
                else:
                    break

            # Valor da entrada
            if opcaoCliente == '1':
                print('\n' * 130)
                valorDeposito = float(input('Qual o valor que vc vai depositar? '))
                saldo += valorDeposito
                print('''
              =============================================
              ========Saldo atualizado com sucesso=========
              -------------- Você tem R$ {} ---------------
              '''.format(saldo))

                desejoEntrada1 = input('''
                        Deseja realizar mais alguma operação como cliente?
                        -------------------Se Sim digite 1----------------------
                        -------------------Se não digite 2----------------------
                        Digite: ''')
                while True:
                    if desejoEntrada1 != '1':
                        if desejoEntrada1 != '2':

                            desejoEntrada1 = input('Por favor digite 1 ou 2: ')
                        else:
                            break
                    else:
                        break

                if desejoEntrada1 == '2':
                    print('\n' * 130)
                    break

            # Visualizar saldo
            elif opcaoCliente == '2':
                print('\n' * 130)
                print('''Seu saldo é de R$ {} '''.format(saldo))

                desejo1 = input('''
           Deseja realizar mais alguma operação como cliente?
        -------------------Se sim digite 1----------------------
        -------------------Se não digite 2----------------------
        Digite: ''')
                while True:
                    if desejo1 != '1':
                        if desejo1 != '2':
                            desejo1 = input('Por favor digite 1 ou 2: ')
                        else:
                            break
                    else:
                        break

                if desejo1 == '2':
                    print('\n' * 130)
                    break

            # Reservar cadeira
            elif opcaoCliente == '3':
                if valorEntrada >= 0.0:
                    if tamanhoTeatro > 0:
                        print('''Reservar cadeira
        
                        O preço do ingresso é R$ {}
        
                          As cadeiras livre são:
                        '''.format(valorEntrada))
                        # imprimir o teatro completo
                        for i in range(1, fileira + 1):
                            for j in range(1, coluna + 1):
                                print("[{}] ".format(j + cont), end=" ")
                            print()
                            cont += coluna
                        cont = 0
                        while True:
                            cadeira = int(input('Qual cadeira você deseja reservar?'))
                            if tamanhoTeatro >= cadeira >= 1:
                                break
                            else:
                                print()
                                print('Por favor, digite um valor entre 1 e {}'.format(tamanhoTeatro))
                                print()

                    else:
                        print()
                        print('O administrador ainda não colocou informações sobre o teatro')
                        print()
                else:
                    print()
                    print('O administrador ainda não colocou informações sobre o teatro')
                    print()

                desejo3 = input('''
           Deseja realizar mais alguma operação como cliente?
        -------------------Se sim digite 1----------------------
        -------------------Se não digite 2----------------------
        Digite: ''')
                while True:
                    if desejo3 != '1':
                        if desejo3 != '2':
                            desejo3 = input('Por favor digite 1 ou 2: ')
                        else:
                            break
                    else:
                        break

                if desejo3 == '2':
                    print('\n' * 130)
                    break
