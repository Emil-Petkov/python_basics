age = int(input())
wash_machine_price = float(input())
price_per_toy = int(input())

money_received = 0
toy_count = 0

for year in range(1, age + 1):
    if year % 2 == 0:
        money_for_year = 10 * (year // 2)
        money_received += money_for_year - 1
    else:
        toy_count += 1

money_from_toys = toy_count * price_per_toy
total_money = money_received + money_from_toys

if total_money >= wash_machine_price:
    print(f"Yes! {total_money - wash_machine_price:.2f}")
else:
    print(f"No! {wash_machine_price - total_money:.2f}")
