day_of_week = input()

price_of_ticket = 0

if day_of_week in ['Monday', 'Tuesday', 'Friday']:
    price_of_ticket = 12

elif day_of_week in ['Wednesday', 'Thursday']:
    price_of_ticket = 14

elif day_of_week in ['Saturday', 'Sunday']:
    price_of_ticket = 16

print(price_of_ticket)
