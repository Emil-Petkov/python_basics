num_pens_packages = int(input())
num_markers_packages = int(input())
liters_of_chalkboard_cleaner = float(input())
percentage_discount = int(input())

price_per_one_pack_pens = 5.80
price_per_one_pack_markers = 7.20
price_per_one_liter_preparation = 1.20

sum_before_discount = ((num_pens_packages * price_per_one_pack_pens) +
                       (num_markers_packages * price_per_one_pack_markers) +
                       (liters_of_chalkboard_cleaner * price_per_one_liter_preparation))

sum_after_discount = sum_before_discount - (sum_before_discount * (percentage_discount / 100))

print(sum_after_discount)
