def operations_between_numbers(num_one: int, num_two: int, operator: str):
    mapper = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if not y == 0 else f'Cannot divide {x} by zero',
        '%': lambda x, y: x % y if not y == 0 else f'Cannot divide {x} by zero',
    }

    if operator in mapper and not num_two == 0:
        result = (mapper[operator](num_one, num_two))

        check_for_even_of_odd = 'even' if result % 2 == 0 else 'odd'

        if operator in ['+', '-', '*']:
            return f'{num_one} {operator} {num_two} = {result} - {check_for_even_of_odd}'

        elif operator == '/':
            return f'{num_one} {operator} {num_two} = {result:.2f}'

        elif operator == '%':
            return f'{num_one} {operator} {num_two} = {result}'

    else:
        return f'Cannot divide {num_one} by zero'


number_one = int(input())
number_two = int(input())
operation = input()
print(operations_between_numbers(number_one, number_two, operation))
