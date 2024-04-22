n_lines = int(input())

even_sum = 0
odd_sum = 0

for num in range(n_lines):
    if num % 2 == 0:
        even_sum += int(input())

    else:
        odd_sum += int(input())

diff = abs(even_sum - odd_sum)

if even_sum == odd_sum:
    print(f'Yes\nSum = {even_sum}')

else:
    print(f'No\nDiff = {diff}')
