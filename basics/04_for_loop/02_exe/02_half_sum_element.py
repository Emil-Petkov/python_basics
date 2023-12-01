import sys

number = int(input())

total_sum = 0

max_num = -sys.maxsize

for iteration in range(1, number + 1):
    current_num = int(input())

    total_sum = total_sum + current_num

    if current_num > max_num:
        max_num = current_num

sum = total_sum - max_num

if sum == max_num:
    print('Yes')
    print(f'Sum = {sum}')
else:
    print("No")
    diff = abs(sum - max_num)
    print(f"Diff = {diff}")
