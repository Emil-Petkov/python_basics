fruit = input()
day_of_week = input()
quantity = float(input())

total = 0

if day_of_week in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
    banana = 2.50
    apple = 1.20
    orange = 0.85
    grapefruit = 1.45
    kiwi = 2.70
    pineapple = 5.50
    grapes = 3.85

    if fruit == 'banana':
        total = banana * quantity

    elif fruit == 'apple':
        total = apple * quantity

    elif fruit == 'orange':
        total = orange * quantity

    elif fruit == 'grapefruit':
        total = grapefruit * quantity

    elif fruit == 'kiwi':
        total = kiwi * quantity

    elif fruit == 'pineapple':
        total = pineapple * quantity

    elif fruit == 'grapes':
        total = grapes * quantity

    else:
        print('error')
        exit()

elif day_of_week in ['Saturday', 'Sunday']:
    banana = 2.70
    apple = 1.25
    orange = 0.90
    grapefruit = 1.60
    kiwi = 3.00
    pineapple = 5.60
    grapes = 4.20

    if fruit == 'banana':
        total = banana * quantity

    elif fruit == 'apple':
        total = apple * quantity

    elif fruit == 'orange':
        total = orange * quantity

    elif fruit == 'grapefruit':
        total = grapefruit * quantity

    elif fruit == 'kiwi':
        total = kiwi * quantity

    elif fruit == 'pineapple':
        total = pineapple * quantity

    elif fruit == 'grapes':
        total = grapes * quantity

    else:
        print('error')
        exit()

else:
    print('error')
    exit()

print(f'{total:.2f}')
