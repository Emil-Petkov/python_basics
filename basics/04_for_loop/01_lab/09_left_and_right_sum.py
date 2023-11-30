n_lines = int(input())

left_sum = 0
right_sum = 0

for n in range(n_lines * 2):
    current_number = int(input())

    if n < n_lines:
        left_sum += current_number

    else:
        right_sum += current_number

if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')

else:
    diff = abs(left_sum - right_sum)

    print(f'No, diff = {diff}')
