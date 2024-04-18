def supplies_for_school(n_pens: int, n_markers: int, liters_board_cleaner: int, discount: int):
    price_packages_pens = 5.80
    price_packages_markers = 7.20
    price_board_cleaner_per_liter = 1.20

    subtotal = ((n_pens * price_packages_pens) + (n_markers * price_packages_markers) +
                (liters_board_cleaner * price_board_cleaner_per_liter))

    ani_discount = subtotal * (discount / 100)

    total = subtotal - ani_discount

    return total


n_packages_pens = int(input())
n_packages_markers = int(input())
liters_board_cleaner = int(input())
discount = int(input())
print(supplies_for_school(n_packages_pens, n_packages_markers, liters_board_cleaner, discount))
