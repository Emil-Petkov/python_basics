def toy_shop(money_for_trip, puzzles, dolls, teddy_bears, minions, trucks):
    price_per_puzzle = 2.60
    price_per_doll = 3.00
    price_per_teddy_bear = 4.10
    price_per_minion = 8.20
    price_per_truck = 2.00

    rent_tax = 0.10

    n_toys = puzzles + dolls + teddy_bears + minions + trucks

    subtotal = ((price_per_puzzle * puzzles) + (price_per_doll * dolls) + (price_per_teddy_bear * teddy_bears) +
                price_per_minion * minions) + (price_per_truck * trucks)

    if n_toys >= 50:
        subtotal -= subtotal * 0.25  # discount - 25%

    subtotal -= subtotal * rent_tax

    total = subtotal

    diff = abs(total - money_for_trip)

    if total >= money_for_trip:
        return f'Yes! {diff:.2f} lv left.'

    else:
        return f'Not enough money! {diff:.2f} lv needed.'


needed_money_for_trip = float(input())
n_puzzles = int(input())
n_dolls = int(input())
n_teddy_bears = int(input())
n_minions = int(input())
n_trucks = int(input())
print(toy_shop(needed_money_for_trip, n_puzzles, n_dolls, n_teddy_bears, n_minions, n_trucks))
