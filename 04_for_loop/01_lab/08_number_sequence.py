import sys

n_lines = int(input())
min_number = sys.maxsize
max_number = -sys.maxsize

for num in range(n_lines):
    current_number = int(input())

    if current_number < min_number:
        min_number = current_number

    if current_number > max_number:
        max_number = current_number

print(f'Max number: {max_number}\nMin number: {min_number}')
