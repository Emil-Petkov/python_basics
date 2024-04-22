def invalid_number(number: int):
    if 100 <= number <= 200 or number == 0:
        return ''

    return 'invalid'


current_number = int(input())
print(invalid_number(current_number))
