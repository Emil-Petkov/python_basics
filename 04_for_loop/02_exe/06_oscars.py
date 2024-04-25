actor_name = input()
points = float(input())
n_judges = int(input())

total_points = points
needed_points = 1250.5

for _ in range(n_judges):
    current_judge = input()
    current_points = float(input())

    total_points += (len(current_judge) * current_points) / 2

    if total_points > needed_points:
        print(f'Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!')
        exit()

diff = abs(total_points - needed_points)

print(f'Sorry, {actor_name} you need {diff:.1f} more!')
