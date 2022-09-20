count_food_packaging_per_dogs = int(input())
count_food_packaging_per_cats = int(input())

price_food_per_dogs = count_food_packaging_per_dogs * 2.50
price_food_per_cats = count_food_packaging_per_cats * 4.00

total = price_food_per_dogs + price_food_per_cats

print(f'{total} lv.')
