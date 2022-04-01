n = input()


if n == "Homem de Ferro" or n == "Hulk" or n == "Capitão América" or n == "Thor" or n == "Gavião Arqueiro" or n == "Viúva Negra":

  p = input()
  e = int(input())

  if n == "Homem de Ferro" and p == "Armadura de Ferro" and e >= 10:
    print("{} conseguiu derrotar Thanos".format(n))
    exit()

  elif n == "Homem de Ferro" and p == "Armadura de Ferro" and e < 10:
    print("{} NAO conseguiu derrotar Thanos, chamem outro Vingador".format(n))
    exit()

  elif n == "Homem de Ferro" and p != "Armadura de Ferro":
    print("{} NAO conseguiu derrotar Thanos".format(n))

    if p == "Força Bruta":
      print("Esse é o poder do Hulk")
      exit()

    elif p == "Escudo":
      print("Esse é o poder do Capitão América")
      exit()

    elif p == "Martelo":
      print("Esse é o poder do Thor")
      exit()

    elif p == "Arco e Flecha":
      print("Esse é o poder do Gavião Arqueiro")
      exit()

    elif p == "Inteligência":
      print("Esse é o poder da Viúva Negra")
      exit()

  elif n == "Hulk" and p == "Força Bruta" and e >= 5:
    print("{} conseguiu derrotar Thanos".format(n))
    exit()

  elif n == "Hulk" and p == "Força Bruta" and e < 5:
    print("{} NAO conseguiu derrotar Thanos, chamem outro Vingador".format(n))
    exit()

  elif n == "Hulk" and p != "Força Bruta":
    print("{} NAO conseguiu derrotar Thanos".format(n))

    if p == "Armadura de Ferro":
      print("Esse é o poder do Homem de Ferro")
      exit()

    elif p == "Escudo":
      print("Esse é o poder do Capitão América")
      exit()

    elif p == "Martelo":
      print("Esse é o poder do Thor")
      exit()

    elif p == "Arco e Flecha":
      print("Esse é o poder do Gavião Arqueiro")
      exit()

    elif p == "Inteligência":
      print("Esse é o poder da Viúva Negra")
      exit()

  elif n == "Capitão América" and p == "Escudo" and e >= 7:
    print("{} conseguiu derrotar Thanos".format(n))
    exit()

  elif n == "Capitão América" and p == "Escudo" and e < 7:
    print("{} NAO conseguiu derrotar Thanos, chamem outro Vingador".format(n))
    exit()

  elif n == "Capitão América" and p != "Escudo":
    print("{} NAO conseguiu derrotar Thanos".format(n))

    if p == "Armadura de Ferro":
      print("Esse é o poder do Homem de Ferro")
      exit()

    elif p == "Força Bruta":
      print("Esse é o poder do Hulk")
      exit()

    elif p == "Martelo":
      print("Esse é o poder do Thor")
      exit()

    elif p == "Arco e Flecha":
      print("Esse é o poder do Gavião Arqueiro")
      exit()

    elif p == "Inteligência":
      print("Esse é o poder da Viúva Negra")
      exit()

  elif n == "Thor" and p == "Martelo" and e >= 4:
    print("{} conseguiu derrotar Thanos".format(n))
    exit()

  elif n == "Thor" and p == "Martelo" and e < 4:
    print("{} NAO conseguiu derrotar Thanos, chamem outro Vingador".format(n))
    exit()

  elif n == "Thor" and p != "Martelo":
    print("{} NAO conseguiu derrotar Thanos".format(n))

    if p == "Armadura de Ferro":
      print("Esse é o poder do Homem de Ferro")
      exit()

    elif p == "Foça Bruta":
      print("Esse é o poder do Hulk")
      exit()

    elif p == "Escudo":
      print("Esse é o poder do Capitão América")
      exit()

    elif p == "Arco e Flecha":
      print("Esse é o poder do Gavião Arqueiro")
      exit()

    elif p == "Inteligência":
      print("Esse é o poder da Viúva Negra")
      exit()

  elif n == "Gavião Arqueiro" and p == "Arco e Flecha" and e >= 12:
    print("{} conseguiu derrotar Thanos".format(n))
    exit()

  elif n == "Gavião Arqueiro" and p == "Arco e Flecha" and e < 12:
    print("{} NAO conseguiu derrotar Thanos, chamem outro Vingador".format(n))
    exit()

  elif n == "Gavião Arqueiro" and p != "Arco e Flecha":
    print("{} NAO conseguiu derrotar Thanos".format(n))

    if p == "Armadura de Ferro":
      print("Esse é o poder do Homem de Ferro")
      exit()

    elif p == "Força Bruta":
      print("Esse é o poder do Hulk")
      exit()

    elif p == "Escudo":
      print("Esse é o poder do Capitão América")
      exit()

    elif p == "Martelo":
      print("Esse é o poder do Gavião Thor")
      exit()

    elif p == "Inteligência":
      print("Esse é o poder da Viúva Negra")
      exit()

  elif n == "Viúva Negra" and p == "Inteligência" and e >= 20:
    print("{} conseguiu derrotar Thanos".format(n))
    exit()

  elif n == "Viúva Negra" and p == "Inteligência" and e < 20:
    print("{} NAO conseguiu derrotar Thanos, chamem outro Vingador".format(n))
    exit()

  elif n == "Viúva Negra" and p != "Inteligência":
    print("{} NAO conseguiu derrotar Thanos".format(n))

    if p == "Armadura de Ferro":
      print("Esse é o poder do Homem de Ferro")
      exit()

    elif p == "Força Bruta":
      print("Esse é o poder do Hulk")
      exit()

    elif p == "Escudo":
      print("Esse é o poder do Capitão América")
      exit()

    elif p == "Martelo":
      print("Esse é o poder do Gavião Thor")
      exit()

    elif p == "Arco e Flecha":
      print("Esse é o poder do Gavião Arqueiro")
      exit()

  elif n == "Viúva Negra" and p == "Inteligência" and e >= 20:
    print("{} conseguiu derrotar Thanos".format(n))
    exit()

else:
  print("Vingador Inválido")
