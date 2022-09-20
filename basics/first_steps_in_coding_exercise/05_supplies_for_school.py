count_pen_packages = int(input())
count_markers_packages = int(input())
liters_of_chalkboard_cleaner = int(input())
discount = int(input())

package_pens = 5.80
package_markers = 7.20
chalkboard_cleaner = 1.20

needed_money = count_pen_packages * package_pens + count_markers_packages * package_markers \
               + liters_of_chalkboard_cleaner * chalkboard_cleaner

sum_after_discount = needed_money - (needed_money * (discount / 100))

print(sum_after_discount)
