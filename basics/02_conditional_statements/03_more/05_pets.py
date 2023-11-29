from math import ceil, floor

days = int(input())
food_in_kg = int(input())
food_per_day_dog_in_kg = float(input())
food_per_day_cat_in_kg = float(input())
food_per_day_turtle_in_grams = float(input())

dog_food = (food_per_day_dog_in_kg * 1000) * days
cat_food = (food_per_day_cat_in_kg * 1000) * days
turtle_food = food_per_day_turtle_in_grams * days

food_per_all_animals = (dog_food + cat_food + turtle_food) / 1000

diff = abs(food_per_all_animals - food_in_kg)

if food_per_all_animals <= food_in_kg:
    print(f'{floor(diff)} kilos of food left.')

else:
    print(f'{ceil(diff)} more kilos of food are needed.')
