type_projection = input()
rows = int(input())
columns = int(input())

total_places_in_hall = rows * columns

total = 0

if type_projection == 'Premiere':
    total = total_places_in_hall * 12.00

elif type_projection == 'Normal':
    total = total_places_in_hall * 7.50

elif type_projection == 'Discount':
    total = total_places_in_hall * 5.00

print(f'{total:.2f} leva')
