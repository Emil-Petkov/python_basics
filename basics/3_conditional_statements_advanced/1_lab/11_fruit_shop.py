type_fruit = input()
day_of_week = input()
quality = float(input())

price = 0

if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' \
        or day_of_week == 'Thursday' or day_of_week == 'Friday':
    if type_fruit == 'banana':
        price = quality * 2.50
        print(f'{price:.2f}')
    elif type_fruit == 'apple':
        price = quality * 1.20
        print(f'{price:.2f}')
    elif type_fruit == 'orange':
        price = quality * 0.85
        print(f'{price:.2f}')
    elif type_fruit == 'grapefruit':
        price = quality * 1.45
        print(f'{price:.2f}')
    elif type_fruit == 'kiwi':
        price = quality * 2.70
        print(f'{price:.2f}')
    elif type_fruit == 'pineapple':
        price = quality * 5.50
        print(f'{price:.2f}')
    elif type_fruit == 'grapes':
        price = quality * 3.85
        print(f'{price:.2f}')
    else:
        print('error')

elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
    if type_fruit == 'banana':
        price = quality * 2.70
        print(f'{price:.2f}')
    elif type_fruit == 'apple':
        price = quality * 1.25
        print(f'{price:.2f}')
    elif type_fruit == 'orange':
        price = quality * 0.90
        print(f'{price:.2f}')
    elif type_fruit == 'grapefruit':
        price = quality * 1.60
        print(f'{price:.2f}')
    elif type_fruit == 'kiwi':
        price = quality * 3.00
        print(f'{price:.2f}')
    elif type_fruit == 'pineapple':
        price = quality * 5.60
        print(f'{price:.2f}')
    elif type_fruit == 'grapes':
        price = quality * 4.20
        print(f'{price:.2f}')
    else:
        print('error')
else:
    print('error')

