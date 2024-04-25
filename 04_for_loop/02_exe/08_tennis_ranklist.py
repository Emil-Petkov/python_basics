n_tournaments = int(input())
points = int(input())

total_points = points
counter_wins = 0

for t in range(n_tournaments):
    current_result = input()

    if current_result == 'W':
        total_points += 2_000
        counter_wins += 1

    elif current_result == 'F':
        total_points += 1_200

    elif current_result == 'SF':
        total_points += 720

average_points = (total_points - points) // n_tournaments

print(f'Final points: {total_points}\nAverage points: {average_points}\n{(counter_wins / n_tournaments) * 100:.2f}%')
