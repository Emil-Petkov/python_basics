def greening(sqm: float):
    price_per_one_sqm = 7.61

    price_per_all_area = sqm * price_per_one_sqm

    discount = price_per_all_area * 0.18
    total_price = price_per_all_area - discount

    return f'The final price is: {total_price:.2f} lv.\nThe discount is: {discount:.2f} lv.'


user_input_sqm = float(input())
result = greening(user_input_sqm)
print(result)
