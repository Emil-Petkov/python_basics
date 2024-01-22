def cinema(type_ticket: str, rows: int, columns: int):
    premiere = 12.00
    normal = 7.50
    discount = 5.00

    places_in_the_hall = rows * columns

    projections = {
        'Premiere': lambda places: places * premiere,
        'Normal': lambda places: places * normal,
        'Discount': lambda places: places * discount,
    }

    calculate_profit = projections[type_ticket](places_in_the_hall)

    return f'{calculate_profit:.2f} leva'


type_projection = input()
rows = int(input())
columns = int(input())

print(cinema(type_projection, rows, columns))
