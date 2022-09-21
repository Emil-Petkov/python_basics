entrance_money = input()

balance = 0

while entrance_money != 'NoMoreMoney':
    current_money = float(entrance_money)
    if current_money <= 0:
        print('Invalid operation!')
        break
    print(f"Increase: {current_money:.2f}")
    balance += current_money
    entrance_money = input()

print(f"Total: {balance:.2f}")
