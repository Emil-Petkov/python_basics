n_tournaments = int(input())
start_points = int(input())

total_points = start_points

count_wins = 0
mapper_points = {
    'W': 2000,
    'F': 1200,
    'SF': 720,
}

for _ in range(n_tournaments):
    current_tournament = input()

    if current_tournament == 'W':
        total_points += mapper_points[current_tournament]
        count_wins += 1

    elif current_tournament == 'F':
        total_points += mapper_points[current_tournament]

    elif current_tournament == 'SF':
        total_points += mapper_points[current_tournament]

print(f'Final points: {total_points}')
print(f'Average points: {(total_points - start_points) // n_tournaments}')
print(f'{(count_wins / n_tournaments) * 100:.2f}%')
