qnt = int(input())
grupo = verificar = 0
maior = cont = 1
for i in range(qnt):
  ordem = int(input())
  if verificar == ordem:
      cont += 1
  else:
      grupo += 1
      if cont > maior:
        maior = cont
      cont = 0
  verificar = ordem
print("groups: {}, biggest: {}".format(grupo, maior+1))