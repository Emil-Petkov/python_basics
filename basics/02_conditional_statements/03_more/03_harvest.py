from math import ceil

vineyard_qm2 = int(input())
grape_per_one_q2m = float(input())
needed_liters_wine = int(input())
num_workers = int(input())

total_grape = vineyard_qm2 * grape_per_one_q2m
wine = total_grape * 0.40 / 2.5

diff = (abs(wine - needed_liters_wine))

if wine >= needed_liters_wine:
    print(f'Good harvest this year! Total wine: {int(wine)} liters.')
    print(f'{ceil(diff)} liters left -> {ceil(diff / num_workers)} liters per person.')

else:
    print(f'It will be a tough winter! More {int(diff)} liters wine needed.')
