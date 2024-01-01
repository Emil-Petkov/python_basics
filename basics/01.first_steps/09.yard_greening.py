def yard_greening(square_meters):
    price_for_one_square_meter = 7.61

    price_before_discount = square_meters * price_for_one_square_meter
    calculated_discount = price_before_discount * 0.18  # 18% discount of total price

    total_bill = price_before_discount - calculated_discount

    return total_bill, calculated_discount


square_meters = float(input())
final_price, discount = yard_greening(square_meters)

print(f'The final price is: {final_price} lv.')
print(f'The discount is: {discount} lv.')
