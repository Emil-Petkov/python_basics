n_combinations = int(input())

left_sum = 0
right_sum = 0

for i in range(n_combinations * 2):
    current_number = int(input())

    if i < n_combinations:
        left_sum += current_number

    else:
        right_sum += current_number

diff = abs(left_sum - right_sum)

if not left_sum == right_sum:
    print(f'No, diff = {diff}')

else:
    print(f'Yes, sum = {left_sum}')
