def hotel_room(month: str, n_nights: int):
    apartment_price = 0
    studio_price = 0

    if month in ['May', 'October']:
        apartment_price = 65 * n_nights
        studio_price = 50 * n_nights

        if n_nights > 14:
            studio_price -= studio_price * 0.30

        elif n_nights > 7:
            studio_price -= studio_price * 0.05

    elif month in ['June', 'September']:
        apartment_price = 68.70 * n_nights
        studio_price = 75.20 * n_nights

        if n_nights > 14:
            studio_price -= studio_price * 0.20

    elif month in ['July', 'August']:
        apartment_price = 77 * n_nights
        studio_price = 76 * n_nights

    if n_nights > 14:
        apartment_price -= apartment_price * 0.10

    return apartment_price, studio_price


month = input()
n_overnight_stays = int(input())
apartment, studio = hotel_room(month, n_overnight_stays)
print(f'Apartment: {apartment:.2f} lv.\nStudio: {studio:.2f} lv.')
