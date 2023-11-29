fuel_type = input()
quantity_fuel = float(input())
club_card = input()

gasoline_price_per_liter = 2.22
diesel_price_per_liter = 2.33
gas_price_per_liter = 0.93

total = 0

if fuel_type == 'Gasoline':
    if club_card == 'Yes':
        total = quantity_fuel * (gasoline_price_per_liter - 0.18)

    elif club_card == 'No':
        total = quantity_fuel * gasoline_price_per_liter

elif fuel_type == 'Diesel':
    if club_card == 'Yes':
        total = quantity_fuel * (diesel_price_per_liter - 0.12)

    elif club_card == 'No':
        total = quantity_fuel * diesel_price_per_liter

elif fuel_type == 'Gas':
    if club_card == 'Yes':
        total = quantity_fuel * (gas_price_per_liter - 0.08)

    elif club_card == 'No':
        total = quantity_fuel * gas_price_per_liter

if 20 <= quantity_fuel <= 25:
    total -= total * 0.08

elif quantity_fuel > 25:
    total -= total * 0.10

print(f'{total:.2f} lv.')
