num_a = int(input())
num_b = int(input())
operator = input()
even_or_odd = ''

result = 0

if operator == '+':
    result = num_a + num_b
    if result % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = 'odd'
    print(f'{num_a} {operator} {num_b} = {result} - {even_or_odd}')

elif operator == '-':
    result = num_a - num_b
    if result % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = 'odd'
    print(f'{num_a} {operator} {num_b} = {result} - {even_or_odd}')

elif operator == '*':
    result = num_a * num_b
    if result % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = 'odd'
    print(f'{num_a} {operator} {num_b} = {result} - {even_or_odd}')

elif operator == '/':
    if num_b == 0:
        print(f'Cannot divide {num_a} by zero')
    else:
        result = num_a / num_b
        print(f'{num_a} / {num_b} = {result:.2f}')

elif operator == '%':
    if num_b == 0:
        print(f'Cannot divide {num_a} by zero')
    else:
        result = num_a % num_b
        print(f'{num_a} % {num_b} = {result}')
