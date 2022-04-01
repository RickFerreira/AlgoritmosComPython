altura = float(input())
raio= float(input())
areaCirculo = (3.14*(raio*raio))
areaTotal = ((areaCirculo*2) + (2*3.14*raio*altura))
volume = (areaCirculo*altura)

print('{:.2f}'.format(volume))
print('{:.2f}'.format(areaTotal))
