def cinema(type_projection: str, rows: int, columns: int):
    total_profit = 0

    projection = {
        'Premiere': 12.00,
        'Normal': 7.50,
        'Discount': 5.00,
    }

    total_seats_in_hall = rows * columns

    total_profit = projection[type_projection] * total_seats_in_hall

    return f'{total_profit:.2f} leva'


type_projection = input()
rows = int(input())
columns = int(input())
print(cinema(type_projection, rows, columns))
