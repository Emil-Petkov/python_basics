qm2 = float(input())

price_per_qm2 = 7.61

needed_money_per_all_area = qm2 * price_per_qm2

discount = needed_money_per_all_area * 0.18

total_price = needed_money_per_all_area - discount

print(f'The final price is: {total_price} lv.')
print(f'The discount is: {discount} lv.')
