def basketball_equipment(tax):
    shoes_price = tax - (tax * 0.40)
    basketball_suit = shoes_price - (shoes_price * 0.20)
    ball_price = basketball_suit / 4
    basketball_accessories = ball_price / 5

    total = tax + shoes_price + basketball_suit + ball_price + basketball_accessories

    return total


year_tax = int(input())
result = basketball_equipment(year_tax)

print(result)
