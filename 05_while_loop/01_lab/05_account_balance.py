command = input()

total = 0

while not command == 'NoMoreMoney':
    current_money = float(command)

    if current_money <= 0:
        print(f'Invalid operation!\nTotal: {total:.2f}')
        break

    total += current_money
    print(f'Increase: {current_money:.2f}')

    command = input()
else:
    print(f'Total: {total:.2f}')
