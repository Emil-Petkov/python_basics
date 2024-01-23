n_age = int(input())
wash_machine = float(input())
toy_price = int(input())

money = 10
count_toys = 0
total = 0
brother_count = 0

for a in range(1, n_age + 1):
    if not a % 2 == 0:
        count_toys += 1

    else:
        brother_count += 1
        total = total + money
        money = money + 10

result = total + (count_toys * toy_price) - brother_count

diff = abs(result - wash_machine)
if result >= wash_machine:
    print(f'Yes! {diff:.2f}')

else:
    print(f'No! {diff:.2f}')
