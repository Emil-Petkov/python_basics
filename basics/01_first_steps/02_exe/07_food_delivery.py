num_chicken_menus = int(input())
num_fish_menus = int(input())
num_vegan_menus = int(input())

price_per_chicken_menu = 10.35
price_per_fish_menu = 12.40
price_per_vegan_menu = 8.15

needed_money_for_menus = (num_chicken_menus * price_per_chicken_menu
                          + (num_fish_menus * price_per_fish_menu) +
                          num_vegan_menus * price_per_vegan_menu)

desert = needed_money_for_menus * 0.20

total_order = needed_money_for_menus + desert + 2.50

print(total_order)
