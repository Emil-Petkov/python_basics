price_for_kg_vegetables = float(input())
price_for_kg_fruits = float(input())

total_kg_vegetables = int(input())
total_kg_fruits = int(input())

total = ((price_for_kg_vegetables * total_kg_vegetables) +
         (price_for_kg_fruits * total_kg_fruits))

convert_price_in_euro = total / 1.94

print(f'{convert_price_in_euro:.2f}')
