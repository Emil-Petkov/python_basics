def basketball_equipment(tax_per_year: int):
    shoes = tax_per_year - (tax_per_year * 0.40)
    suit = shoes - (shoes * 0.20)
    ball = suit / 4
    other = ball / 5

    result = tax_per_year + shoes + suit + ball + other

    return result


basketball_tax = int(input())
print(basketball_equipment(basketball_tax))
