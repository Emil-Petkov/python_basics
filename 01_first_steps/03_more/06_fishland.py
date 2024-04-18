def fish_store(price_mackerel_kg, price_sprinkle_kg, kg_bonito, kg_safrid, kg_mussels):
    price_bonito = price_mackerel_kg * 1.60
    price_safrid = price_sprinkle_kg * 1.80
    price_mussels = 7.50  # fixed price

    result = (kg_bonito * price_bonito) + (kg_safrid * price_safrid) + (kg_mussels * price_mussels)

    return f'{result:.2f}'


price_mackerel_kg = float(input())
price_sprinkle_kg = float(input())
kg_bonito = float(input())
kg_safrid = float(input())
kg_mussels = int(input())
print(fish_store(price_mackerel_kg, price_sprinkle_kg, kg_bonito, kg_safrid, kg_mussels))
