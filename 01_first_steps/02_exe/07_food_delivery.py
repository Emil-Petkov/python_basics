def food_delivery(chicken_menus: int, fish_menus: int, vegan_menus: int):
    price_per_one_chicken_menu = 10.35
    price_per_one_fish_menu = 12.40
    price_per_one_vegan_menu = 8.15

    fixed_delivery_tax = 2.50

    price_per_all_menus = ((chicken_menus * price_per_one_chicken_menu) +
                           (fish_menus * price_per_one_fish_menu) +
                           vegan_menus * price_per_one_vegan_menu)

    price_per_desert = price_per_all_menus * 0.20

    total = price_per_all_menus + price_per_desert + fixed_delivery_tax

    return total


n_chicken_menus = int(input())
n_fish_menus = int(input())
n_vegan_menus = int(input())
print(food_delivery(n_chicken_menus, n_fish_menus, n_vegan_menus))
