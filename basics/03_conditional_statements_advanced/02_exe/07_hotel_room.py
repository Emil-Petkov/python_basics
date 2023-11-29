month_of_year = input()
overnight_stays = int(input())

apartment_price = 0
studio_price = 0

if month_of_year in ['May', 'October', ]:
    if overnight_stays > 14:
        studio_price = (overnight_stays * 50) - ((overnight_stays * 50) * 0.30)

    else:
        if overnight_stays > 7:
            studio_price = (overnight_stays * 50) - ((overnight_stays * 50) * 0.05)

        else:
            studio_price = (overnight_stays * 50)

    if overnight_stays > 14:
        apartment_price = (overnight_stays * 65) - ((overnight_stays * 65) * 0.10)

    else:
        apartment_price = (overnight_stays * 65)

elif month_of_year in ['June', 'September', ]:
    if overnight_stays > 14:
        studio_price = (overnight_stays * 75.20) - ((overnight_stays * 75.20) * 0.20)

    else:
        studio_price = (overnight_stays * 75.20)

    if overnight_stays > 14:
        apartment_price = (overnight_stays * 68.70) - ((overnight_stays * 68.70) * 0.10)

    else:
        apartment_price = (overnight_stays * 68.70)

elif month_of_year in ['July', 'August', ]:
    if overnight_stays > 14:
        apartment_price = (overnight_stays * 77) - ((overnight_stays * 77) * 0.10)

    else:
        apartment_price = (overnight_stays * 77)

    studio_price = (overnight_stays * 76)

print(f'Apartment: {apartment_price:.2f} lv.')
print(f'Studio: {studio_price:.2f} lv.')
