num_one = int(input())
num_two = int(input())
operator = input()

if operator == '+':
    result = num_one + num_two

    if result % 2 == 0:
        print(f'{num_one} + {num_two} = {result} - even')

    else:
        print(f'{num_one} + {num_two} = {result} - odd')

elif operator == '-':
    result = num_one - num_two

    if result % 2 == 0:
        print(f'{num_one} - {num_two} = {result} - even')

    else:
        print(f'{num_one} - {num_two} = {result} - odd')

elif operator == '*':
    result = num_one * num_two

    if result % 2 == 0:
        print(f'{num_one} * {num_two} = {result} - even')

    else:
        print(f'{num_one} * {num_two} = {result} - odd')


elif operator == '/':
    if num_two == 0:
        print(f'Cannot divide {num_one} by zero')

    else:
        result = num_one / num_two

        print(f'{num_one} / {num_two} = {result:.2f}')

elif operator == '%':
    if num_two == 0:
        print(f'Cannot divide {num_one} by zero')

    else:
        result = num_one % num_two

        print(f'{num_one} % {num_two} = {result}')