n = int(input())

special_numbers = []

for number in range(1111, 10000):
    is_special = True
    for digit in str(number):
        if int(digit) == 0 or n % int(digit) != 0:
            is_special = False
            break
    if is_special:
        special_numbers.append(number)

print(" ".join(map(str, special_numbers)))
