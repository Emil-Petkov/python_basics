def hotel_room(month_of_year: str, n_nights: int):
    if month_of_year in ['May', 'October']:
        base_rate_studio = 50.00
        base_rate_apartment = 65.00

    elif month_of_year in ['June', 'September']:
        base_rate_studio = 75.20
        base_rate_apartment = 68.70

    elif month_of_year in ['July', 'August']:
        base_rate_studio = 76.00
        base_rate_apartment = 77.00

    rent_per_studio = base_rate_studio * n_nights
    rent_per_apartment = base_rate_apartment * n_nights

    if month_of_year in ['May', 'October']:
        if n_nights > 14:
            rent_per_studio *= 0.70

        elif n_nights > 7:
            rent_per_studio *= 0.95

    elif month_of_year in ['June', 'September'] and n_nights > 14:
        rent_per_studio *= 0.80  # 20%

    if n_nights > 14:
        rent_per_apartment *= 0.90

    return f'Apartment: {rent_per_apartment:.2f} lv.\nStudio: {rent_per_studio:.2f} lv.'


month_of_year = input()
n_nights = int(input())

print(hotel_room(month_of_year, n_nights))
