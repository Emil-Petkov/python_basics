def bonus_score(points: int):
    bonus_points = 0

    if points <= 100:
        bonus_points += 5

    elif points > 1000:
        bonus_points += points * 0.10

    else:
        bonus_points += points * 0.20

    if points % 2 == 0:
        bonus_points += 1

    elif points % 5 == 0:
        bonus_points += 2

    total_points = points + bonus_points

    return f'{bonus_points}\n{total_points}'


current_points = int(input())
print(bonus_score(current_points))
