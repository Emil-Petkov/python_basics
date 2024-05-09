start_number = int(input())
end_number = int(input())

for current_num in range(start_number, end_number + 1):

    even_sum = 0
    odd_sum = 0

    for index, str_num in enumerate(str(current_num)):
        if index % 2 == 0:
            even_sum += int(str_num)

        else:
            odd_sum += int(str_num)

    if even_sum == odd_sum:
        print(current_num, end=' ')
