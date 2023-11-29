pool_capacity_in_liters = int(input())
capacity_of_the_first_tube_per_hour = int(input())
capacity_of_the_second_tube_per_hour = int(input())
hours = float(input())

first_tube = capacity_of_the_first_tube_per_hour * hours
second_tube = capacity_of_the_second_tube_per_hour * hours

total_capacity_of_the_tube = first_tube + second_tube

pool_completed = (total_capacity_of_the_tube / pool_capacity_in_liters) * 100
first_tube_in_percentage = (first_tube / total_capacity_of_the_tube) * 100
second_tube_in_percentage = (second_tube / total_capacity_of_the_tube) * 100

if total_capacity_of_the_tube > pool_capacity_in_liters:
    diff = abs(pool_capacity_in_liters - total_capacity_of_the_tube)

    print(f'For {hours:.2f} hours the pool overflows with {diff:.2f} liters.')

else:
    print(
        f'The pool is {pool_completed:.2f}% full. Pipe 1: {first_tube_in_percentage:.2f}%. Pipe 2: {second_tube_in_percentage:.2f}%.')
