count_chicken_menu = int(input())
count_fish_menu = int(input())
count_vegan_menu = int(input())

chicken_menu_price = 10.35
fish_menu_price = 12.40
vegan_menu_price = 8.15

sum = count_chicken_menu * chicken_menu_price + count_fish_menu * fish_menu_price \
      + count_vegan_menu * vegan_menu_price

desert = sum * 0.20

total = sum + desert + 2.50

print(total)
