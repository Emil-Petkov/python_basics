num_chrysanthemums = int(input())
num_roses = int(input())
num_tulips = int(input())
season_of_year = input()
is_holiday = input()

total_num_of_flowers = num_chrysanthemums + num_roses + num_tulips

arranging_a_bouquet = 2.00

total = 0

if season_of_year in ['Spring', 'Summer']:
    chrysanthemums_price = 2.00
    roses_price = 4.10
    tulips_price = 2.50

    total += ((num_chrysanthemums * chrysanthemums_price)
              + (num_roses * roses_price)
              + (num_tulips * tulips_price)
              )

elif season_of_year in ['Autumn', 'Winter']:
    chrysanthemums_price = 3.75
    roses_price = 4.50
    tulips_price = 4.15

    total += ((num_chrysanthemums * chrysanthemums_price)
              + (num_roses * roses_price)
              + (num_tulips * tulips_price)
              )

if is_holiday == 'Y':
    total *= 1.15

if season_of_year == 'Spring' and num_tulips > 7:
    total -= total * 0.05

elif season_of_year == 'Winter' and num_roses >= 10:
    total -= total * 0.10

if total_num_of_flowers > 20:
    total -= total * 0.20

total += arranging_a_bouquet

print(f'{total:.2f}')
