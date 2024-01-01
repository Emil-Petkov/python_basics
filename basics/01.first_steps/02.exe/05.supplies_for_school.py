def supplies_for_school(n_packages_pens: int, n_packages_markers: int, n_liters_board_preparation: int, discount: int):
    price_for_package_pens = 5.80
    price_for_package_markers = 7.20
    price_for_liters_board_preparation = 1.20

    total_bill = ((n_packages_pens * price_for_package_pens) + (n_packages_markers * price_for_package_markers) +
                  (n_liters_board_preparation * price_for_liters_board_preparation))

    return total_bill - (total_bill * (discount / 100))


packages_pens = int(input())
packages_markers = int(input())
board_preparation = int(input())
percent_discount = int(input())

result = supplies_for_school(packages_pens, packages_markers, board_preparation, percent_discount)

print(result)
