needed_money = float(input())
owned_money = float(input())

days_counter = 0
spending_counter = 0

while owned_money < needed_money:
    if spending_counter == 5:
        break

    command = input()
    money = float(input())
    days_counter += 1

    if command == 'save':
        owned_money += money
        spending_counter = 0

    elif command == 'spend':
        owned_money -= money
        spending_counter += 1

        if owned_money < 0:
            owned_money = 0

if spending_counter == 5:
    print(f"You can't save the money.\n{days_counter}")

else:
    print(f'You saved the money for {days_counter} days.')