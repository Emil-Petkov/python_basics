days = int(input()) - 1
type_room = input()
grade = input()

price = 0

if type_room == 'room for one person':
    price = days * 18
elif type_room == 'apartment':
    if days < 10:
        price = (days * 25) * 0.70
    elif days <= 15:
        price = (days * 25) * 0.65
    elif days > 15:
        price = (days * 25) * 0.50
elif type_room == 'president apartment':
    if days < 10:
        price = (days * 35) * 0.90
    elif days <= 15:
        price = (days * 35) * 0.85
    elif days > 15:
        price = (days * 35) * 0.80

if grade == 'positive':
    price *= 1.25
elif grade == 'negative':
    price *= 0.90

print(f'{price:.2f}')
