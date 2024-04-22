def operations_between_numbers(f_num: int, s_num: int, operator: str):
    operatons = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: f'Cannot divide {f_num} by zero' if s_num == 0 else x / y,
        '%': lambda x, y: f'Cannot divide {f_num} by zero' if s_num == 0 else x % y,
    }

    calculate = operatons[operator](f_num, s_num)

    if operator in ['+', '-', '*']:
        even_or_odd = 'even' if calculate % 2 == 0 else 'odd'

        return f'{f_num} {operator} {s_num} = {calculate} - {even_or_odd}'

    elif operator == '/':
        if s_num == 0:
            return calculate

        return f'{f_num} {operator} {s_num} = {calculate:.2f}'

    elif operator == '%':
        if s_num == 0:
            return calculate

        return f'{f_num} {operator} {s_num} = {calculate}'


first_number = int(input())
second_number = int(input())
operator = input()

result = operations_between_numbers(first_number, second_number, operator)
print(result)
