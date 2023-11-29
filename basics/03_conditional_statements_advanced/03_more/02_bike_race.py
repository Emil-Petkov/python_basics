juniors_cyclist = int(input())
seniors_cyclist = int(input())
track_type = input()

tax = 0

if track_type == 'trail':
    tax += juniors_cyclist * 5.50
    tax += seniors_cyclist * 7

elif track_type == 'cross-country':
    tax += juniors_cyclist * 8
    tax += seniors_cyclist * 9.50

    if juniors_cyclist + seniors_cyclist >= 50:
        tax -= tax * 0.25

elif track_type == 'downhill':
    tax += juniors_cyclist * 12.25
    tax += seniors_cyclist * 13.75

elif track_type == 'road':
    tax += juniors_cyclist * 20
    tax += seniors_cyclist * 21.50

prize_fund = tax - (tax * 0.05)

print(f'{prize_fund:.2f}')
