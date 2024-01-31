command = input()

while not command == 'End':
    budget = float(input())

    while True:
        saved_money = float(input())

        budget -= saved_money

        if budget <= 0:
            print(f'Going to {command}!')
            break

    command = input()
