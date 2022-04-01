codigo,quantidade = input().split(" ")
codigo = int(codigo)
quantidade = int(quantidade)

if (codigo == 1):
    print("Total: R$ {:.2f}".format(quantidade*4))
elif (codigo == 2):
    print("Total: R$ {:.2f}".format(quantidade*4.5))
elif (codigo == 3):
    print("Total: R$ {:.2f}".format(quantidade*5))
elif (codigo == 4):
    print("Total: R$ {:.2f}".format(quantidade*2))
else:
    print("Total: R$ {:.2f}".format(quantidade *1.5))