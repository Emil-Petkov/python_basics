def vegetable_market(price_kg_vegetables: float, price_kg_fruits: float, kg_vegetables: float, kg_fruits: float):
    result = (price_kg_vegetables * kg_vegetables) + (price_kg_fruits * kg_fruits)
    convert_result_in_euro = result / 1.94

    return f'{convert_result_in_euro:.2f}'


price_per_kg_vegetables = float(input())
price_per_kg_fruits = float(input())
total_kg_vegetables = int(input())
total_kg_fruits = int(input())
print(vegetable_market(price_per_kg_vegetables, price_per_kg_fruits, total_kg_vegetables, total_kg_fruits))
