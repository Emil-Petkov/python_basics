type_projection = input()
rows = int(input())
columns = int(input())

price = 0

area_of_salon = rows * columns

if type_projection == 'Premiere':
    price = 12.00
elif type_projection == 'Normal':
    price = 7.50
elif type_projection == 'Discount':
    price = 5.00

calculate_profit = area_of_salon * price

print(f'{calculate_profit:.2f} leva')
