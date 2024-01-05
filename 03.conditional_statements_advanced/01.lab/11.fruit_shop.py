def fruit_shop(fruit: str, day_of_week: str, quantity: float):
    workdays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',)
    weekdays = ('Saturday', 'Sunday')

    calc_mapper = {
        workdays: {

            'banana': 2.50,
            'apple': 1.20,
            'orange': 0.85,
            'grapefruit': 1.45,
            'kiwi': 2.70,
            'pineapple': 5.50,
            'grapes': 3.85,

        },
        weekdays: {

            'banana': 2.70,
            'apple': 1.25,
            'orange': 0.90,
            'grapefruit': 1.60,
            'kiwi': 3.00,
            'pineapple': 5.60,
            'grapes': 4.20,

        }
    }

    if day_of_week not in workdays and day_of_week not in weekdays:
        return 'error'

    price_list = calc_mapper[workdays] if day_of_week in workdays else calc_mapper[weekdays]

    if fruit not in price_list:
        return 'error'

    price = price_list[fruit] * quantity
    return f'{price:.2f}'


fruit = input()
day_of_week = input()
quantity = float(input())

print(fruit_shop(fruit, day_of_week, quantity))
