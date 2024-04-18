def even_or_odd(number: int):
    if number % 2 == 0:
        return 'even'

    else:
        return 'odd'


current_number = int(input())
print(even_or_odd(current_number))
