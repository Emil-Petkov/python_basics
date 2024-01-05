def number_in_range(num: int):
    if -100 <= num <= 100 and not num == 0:
        return 'Yes'
    else:
        return 'No'


number = int(input())
print(number_in_range(number))
