def pet_shop(dog_food_pack: int, cat_food_pack: int):
    price_for_one_pack_dog_food = 2.50
    price_for_one_pack_cat_food = 4.00

    calculate = ((dog_food_pack * price_for_one_pack_dog_food) +
                 (cat_food_pack * price_for_one_pack_cat_food))

    return f'{calculate} lv.'


dog_food_pack = int(input())
cat_food_pack = int(input())
result = pet_shop(dog_food_pack, cat_food_pack)

print(result)
