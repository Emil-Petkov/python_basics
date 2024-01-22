def even_or_odd(number: int):
    return 'even' if number % 2 == 0 else 'odd'


number = int(input())
print(even_or_odd(number))
