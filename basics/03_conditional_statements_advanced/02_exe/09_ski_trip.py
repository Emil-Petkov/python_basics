days = int(input()) - 1
type_room = input()
rate = input()

total = 0

if type_room == 'room for one person':
    total += days * 18

elif type_room == 'apartment':
    if days < 10:
        total += (days * 25) - ((days * 25) * 0.30)

    elif 10 <= days <= 15:
        total += (days * 25) - ((days * 25) * 0.35)

    elif days > 15:
        total += (days * 25) - ((days * 25) * 0.50)

elif type_room == 'president apartment':
    if days < 10:
        total += (days * 35) - ((days * 35) * 0.10)

    elif 10 <= days <= 15:
        total += (days * 35) - ((days * 35) * 0.15)

    elif days > 15:
        total += (days * 35) - ((days * 35) * 0.20)

if rate == 'positive':
    total *= 1.25

elif rate == 'negative':
    total -= total * 0.10

print(f'{total:.2f}')
