


money = float(input('Ввести сумму:'))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
deposit.append(money*5.6/100)
deposit.append(money*5.9/100)
deposit.append(money*4.28/100)
deposit.append(money*4/100)
print(deposit)

print('Максимальная сумма, которую вы можете заработать', max(deposit))

