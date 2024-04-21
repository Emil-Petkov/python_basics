def new_house(type_flower, n_flowers, budget):
    prices = {
        'Roses': 5.00,
        'Dahlias': 3.80,
        'Tulips': 2.80,
        'Narcissus': 3.00,
        'Gladiolus': 2.50,
    }

    calculate_price = n_flowers * prices[type_flower]

    if n_flowers > 80 and type_flower == 'Roses':
        calculate_price -= calculate_price * 0.10

    elif n_flowers > 90 and type_flower == 'Dahlias':
        calculate_price -= calculate_price * 0.15

    elif n_flowers > 80 and type_flower == 'Tulips':
        calculate_price -= calculate_price * 0.15

    elif n_flowers < 120 and type_flower == 'Narcissus':
        calculate_price *= 1.15

    elif n_flowers < 80 and type_flower == 'Gladiolus':
        calculate_price *= 1.20

    diff = abs(budget - calculate_price)

    if budget >= calculate_price:
        return f'Hey, you have a great garden with {n_flowers} {type_flower} and {diff:.2f} leva left.'

    return f'Not enough money, you need {diff:.2f} leva more.'


type_flower = input()
n_flowers = int(input())
budget = int(input())
print(new_house(type_flower, n_flowers, budget))
