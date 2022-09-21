type_flowers = input()
count_flowers = int(input())
budget = int(input())

price = 0
needed_money = 0

if type_flowers == 'Roses':
    price = 5.00
    if count_flowers > 80:
        needed_money = (count_flowers * price) * 0.90
    else:
        needed_money = count_flowers * price
elif type_flowers == 'Dahlias':
    price = 3.80
    if count_flowers > 90:
        needed_money = (count_flowers * price) * 0.85
    else:
        needed_money = count_flowers * price
elif type_flowers == 'Tulips':
    price = 2.80
    if count_flowers > 80:
        needed_money = (count_flowers * price) * 0.85
    else:
        needed_money = count_flowers * price
elif type_flowers == 'Narcissus':
    price = 3.00
    if count_flowers < 120:
        needed_money = (count_flowers * price) * 1.15
    else:
        needed_money = count_flowers * price
elif type_flowers == 'Gladiolus':
    price = 2.50
    if count_flowers < 80:
        needed_money = (count_flowers * price) * 1.20
    else:
        needed_money = count_flowers * price

difference = abs(budget - needed_money)

if budget >= needed_money:
    print(f'Hey, you have a great garden with {count_flowers} {type_flowers} and {difference:.2f} leva left.')
else:
    print(f'Not enough money, you need {difference:.2f} leva more.')
