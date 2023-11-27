q_m2 = float(input())

price_per_one_q_m2_greening = 7.61

discount = 0.18  # percent discount

price_before_discount = q_m2 * price_per_one_q_m2_greening

price_after_discount = price_before_discount - (price_before_discount * discount)
total_discount = price_before_discount * discount

print(f'The final price is: {price_after_discount:.2f} lv.')
print(f'The discount is: {total_discount:.2f} lv.')
