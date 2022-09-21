destination = input()

while destination != 'End':
    needed_money = float(input())
    piggy_bank = 0

    while piggy_bank < needed_money:
        current_money = float(input())
        piggy_bank += current_money
    print(f"Going to {destination}!")
    destination = input()
