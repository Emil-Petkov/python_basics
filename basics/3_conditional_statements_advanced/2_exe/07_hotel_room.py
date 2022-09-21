month = input()
nights_count = int(input())

studio_per_night = 0
apartment_per_night = 0

if month == 'May' or month == 'October':
    studio_per_night = 50
    apartment_per_night = 65

    if nights_count > 14:
        studio_per_night = studio_per_night * 0.70
    elif nights_count > 7:
        studio_per_night = studio_per_night * 0.95

elif month == 'June' or month == 'September':
    studio_per_night = 75.20
    apartment_per_night = 68.70

    if nights_count > 14:
        studio_per_night = studio_per_night * 0.80

elif month == 'July' or month == 'August':
    studio_per_night = 76
    apartment_per_night = 77

if nights_count > 14:
    apartment_per_night = apartment_per_night * 0.90

total_price_studio = abs(nights_count * studio_per_night)
total_price_apartment = abs(nights_count * apartment_per_night)

print(f'Apartment: {total_price_apartment:.2f} lv.')
print(f'Studio: {total_price_studio:.2f} lv.')