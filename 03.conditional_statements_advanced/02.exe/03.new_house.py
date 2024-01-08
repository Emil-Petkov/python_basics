










def new_house(type_of_flower: str, n_flowers: int, budget: int):
    # price
    rose_price = 5.00
    dahlias_price = 3.80
    tulips_price = 2.80
    narcissus_price = 3.00
    gladiolus_price = 2.50

    total = 0

    if type_of_flower == 'Roses':
        total = n_flowers * rose_price

        if n_flowers > 80:
            total -= total * 0.10

    elif type_of_flower == 'Dahlias':
        total = n_flowers * dahlias_price

        if n_flowers > 90:
            total -= total * 0.15

    elif type_of_flower == 'Tulips':
        total = n_flowers * tulips_price

        if n_flowers > 80:
            total -= total * 0.15

    elif type_of_flower == 'Narcissus':
        total = n_flowers * narcissus_price

        if n_flowers < 120:
            total = total * 1.15

    elif type_of_flower == 'Gladiolus':
        total = n_flowers * gladiolus_price

        if n_flowers < 80:
            total = total * 1.20

    diff = abs(budget - total)
    if total <= budget:
        return f'Hey, you have a great garden with {n_flowers} {type_of_flower} and {diff:.2f} leva left.'

    return f'Not enough money, you need {diff:.2f} leva more.'


type_of_flower = input()
n_flowers = int(input())
budget = int(input())
print(new_house(type_of_flower, n_flowers, budget))
