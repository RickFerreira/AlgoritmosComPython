data = input('Digite a data no formato dd/mm/aaaa: ')

dia, mes, ano = map(int, data.split('/'))

meses = {
    1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril',
    5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto',
    9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'
}

print('{:02} de {} de {}'.format(dia, meses[mes], ano))
