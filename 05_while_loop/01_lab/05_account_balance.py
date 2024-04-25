money = input()
total = 0

while not money == 'NoMoreMoney':
    if float(money) > 0:
        total += float(money)
        print(f'Increase: {float(money):.2f}')

    else:
        print('Invalid operation!')
        break

    money = input()

print(f'Total: {total:.2f}')
