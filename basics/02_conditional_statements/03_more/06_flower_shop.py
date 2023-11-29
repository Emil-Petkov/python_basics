from math import floor, ceil

num_magnolias = int(input())
num_hyacinths = int(input())
num_roses = int(input())
num_cacti = int(input())
gift_price = float(input())

price_per_magnolia = 3.25
price_per_hyacinth = 4.00
price_per_rose = 3.50
price_per_cactus = 8.00

total = 0

order = ((num_magnolias * price_per_magnolia) +
         (num_hyacinths * price_per_hyacinth) +
         (num_roses * price_per_rose) +
         (num_cacti * price_per_cactus))

taxes = order * 0.05

total += order - taxes

diff = abs(total - gift_price)

if total >= gift_price:
    print(f'She is left with {floor(diff)} leva.')

else:
    print(f'She will have to borrow {ceil(diff)} leva.')
