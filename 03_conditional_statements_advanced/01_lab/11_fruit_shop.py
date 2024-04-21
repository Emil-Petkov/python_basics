def fruit_shop(fruit, day_of_week, quantity):
    price = 0

    week_price = {
        'banana': 2.50,
        'apple': 1.20,
        'orange': 0.85,
        'grapefruit': 1.45,
        'kiwi': 2.70,
        'pineapple': 5.50,
        'grapes': 3.85,
    }

    weekend_price = {
        'banana': 2.70,
        'apple': 1.25,
        'orange': 0.90,
        'grapefruit': 1.60,
        'kiwi': 3.00,
        'pineapple': 5.60,
        'grapes': 4.20,
    }

    work_day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', ]
    weekend = ['Saturday', 'Sunday', ]

    if (day_of_week in work_day or day_of_week in weekend) and (fruit in week_price):

        if day_of_week in work_day:
            price = week_price[fruit] * quantity

        elif day_of_week in weekend:
            price = weekend_price[fruit] * quantity

    else:
        return 'error'

    return f'{price:.2f}'


fruit = input()
day_of_week = input()
quantity = float(input())
print(fruit_shop(fruit, day_of_week, quantity))
