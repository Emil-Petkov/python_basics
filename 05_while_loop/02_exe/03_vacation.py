







trip_price = float(input())
current_money = float(input())
counter_days = 0
consecutive_spend_days = 0

while current_money < trip_price and consecutive_spend_days < 5:
    action = input()
    amount = float(input())
    counter_days += 1

    if action == "spend":
        current_money -= amount

        if current_money < 0:
            current_money = 0
        consecutive_spend_days += 1

    elif action == "save":
        current_money += amount
        consecutive_spend_days = 0

    if current_money >= trip_price:
        print(f"You saved the money for {counter_days} days.")
        break

    elif consecutive_spend_days == 5:
        print("You can't save the money.")
        print(counter_days)
