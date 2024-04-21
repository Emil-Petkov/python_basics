def number_in_range(num: int):
    if not num == 0 and (-100 <= num <= 100):
        return 'Yes'

    else:
        return 'No'


4
number = int(input())
print(number_in_range(number))
