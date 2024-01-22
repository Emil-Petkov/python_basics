def food_delivery(n_chicken_menus: int, n_fish_menus: int, n_vegan_menus: int):
    price_for_chicken_menu = 10.35
    price_for_fish_menu = 12.40
    price_for_vegan_menu = 8.15
    delivery = 2.50  # fixed price

    subtotal = ((n_chicken_menus * price_for_chicken_menu) + (n_fish_menus * price_for_fish_menu) +
                (n_vegan_menus * price_for_vegan_menu))

    desert = subtotal * 0.20

    total_bill = subtotal + desert + delivery

    return total_bill


n_chicken_menus = int(input())
n_fish_menus = int(input())
n_vegan_menus = int(input())

result = food_delivery(n_chicken_menus, n_fish_menus, n_vegan_menus)

print(result)
