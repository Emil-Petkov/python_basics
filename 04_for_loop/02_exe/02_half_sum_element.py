













import sys

n_numbers = int(input())

max_numbers = -sys.maxsize
sum_of_numbers = 0

for num in range(n_numbers):
    current_number = int(input())

    sum_of_numbers += current_number

    if current_number > max_numbers:
        max_numbers = current_number

result = sum_of_numbers - max_numbers

if result == max_numbers:
    print(f'Yes\nSum = {result}')

else:
    diff = abs(result - max_numbers)
    print(f'No\nDiff = {diff}')
