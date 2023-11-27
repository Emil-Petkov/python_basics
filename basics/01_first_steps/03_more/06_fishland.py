mackerel_price = float(input())
sprat_fish_price = float(input())
bonito_kg = float(input())
safrid_kg = float(input())
mussels_kg = int(input())

bonito_price = mackerel_price * 1.60
safrid_price = sprat_fish_price * 1.80
mussels_price = 7.50

calculate = (bonito_kg * bonito_price) + (safrid_kg * safrid_price) + (mussels_kg * mussels_price)

print(f'{calculate:.2f}')
