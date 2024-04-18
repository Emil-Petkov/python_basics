def pet_shop(n_dog_food_packages, n_cat_food_packages):
    price_per_one_pack_for_dog = 2.50
    price_per_one_pack_for_cat = 4.00

    total_sum = (n_dog_food_packages * price_per_one_pack_for_dog) + (n_cat_food_packages * price_per_one_pack_for_cat)

    return f'{total_sum} lv.'


dog_food_packages = int(input())
cat_food_packages = int(input())
print(pet_shop(dog_food_packages, cat_food_packages))
