n_kilometers = int(input())
part_of_day = input()

total_price = 0

if n_kilometers >= 100:
    total_price = n_kilometers * 0.06

elif n_kilometers >= 20:
    total_price = n_kilometers * 0.09

else:
    if part_of_day == 'day':
        total_price = 0.70 + (n_kilometers * 0.79)

    elif part_of_day == 'night':
        total_price = 0.70 + (n_kilometers * 0.90)

print(f'{total_price:.2f}')
