year_tax = int(input())

basketball_shoes_price = year_tax - (year_tax * 0.40)
basketball_suit_price = basketball_shoes_price - (basketball_shoes_price * 0.20)
ball_price = basketball_suit_price / 4
others = ball_price / 5

total = year_tax + basketball_shoes_price + basketball_suit_price + ball_price + others

print(total)
