medio = input()
fez = input()
nota = int(input())
escola = input()
renda = float(input())

if medio != 'CLD' and medio != 'CVC' and medio != 'CSC' and medio != 'NCC':
    print('Informacao sobre ensino medio invalida')

elif medio == 'CLD' or medio == 'CVC':
    if fez == 's':
        if 800 >= nota >= 400:
            if escola == 'PUB' or escola == 'PCB':
                if renda <= 1431.00:
                    print('Voce terah direito a isencao')
                else:
                    print('Infelizmente voce nao tem direito a isencao')
            else:
                print('Infelizmente voce nao tem direito a isencao')

        elif escola == 'PUB' or escola == 'PCB':
            if renda <= 1431.00:
                    print('Voce terah direito a isencao')
            else:
                    print('Infelizmente voce nao tem direito a isencao')
        else:
            print('Infelizmente voce nao tem direito a isencao')

    elif escola == 'PUB' or escola == 'PCB':
        if renda <= 1431.00:
            print('Voce terah direito a isencao')
        elif escola == 'PUB' or escola == 'PCB':
            print('Voce terah direito a isencao')
        else:
            print('Infelizmente voce nao tem direito a isencao')
    else:
        print('Infelizmente voce nao tem direito a isencao')
else:
    print('Infelizmente voce nao tem direito a isencao')
