def toy_shop(trip_price: float, n_puzzles: int, n_dolls: int, n_teddy_bear: int, n_minions: int, n_trucks: int):
    puzzle = 2.60
    doll = 3.00
    teddy_bear = 4.10
    minion = 8.20
    truck = 2.00

    subtotal = ((n_puzzles * puzzle) + (n_dolls * doll) + (n_teddy_bear * teddy_bear) +
                (n_minions * minion) + (n_trucks * truck))

    total_toy_count = n_puzzles + n_dolls + n_teddy_bear + n_minions + n_trucks

    if total_toy_count >= 50:
        profit_of_toys = subtotal - (subtotal * 0.25)

    else:
        profit_of_toys = subtotal

    price_after_store_rent = profit_of_toys - (profit_of_toys * 0.10)

    diff = abs(price_after_store_rent - trip_price)

    if price_after_store_rent >= trip_price:
        return f'Yes! {diff:.2f} lv left.'

    else:
        return f'Not enough money! {diff:.2f} lv needed.'


price_for_trip = float(input())
n_puzzles = int(input())
n_dolls = int(input())
n_teddy_bear = int(input())
n_minions = int(input())
n_trucks = int(input())

print(toy_shop(price_for_trip, n_puzzles, n_dolls, n_teddy_bear, n_minions, n_trucks))
