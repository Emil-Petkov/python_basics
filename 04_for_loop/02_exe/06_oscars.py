actor_name = input()
points = float(input())
n_judging_panel = int(input())

for _ in range(n_judging_panel):
    judge_name = input()
    judge_points = float(input())

    points += ((len(judge_name) * judge_points) / 2)

    if points > 1250.5:
        print(f'Congratulations, {actor_name} got a nominee for leading role with {points:.1f}!')
        break

else:
    diff = abs(points - 1250.5)
    print(f'Sorry, {actor_name} you need {diff:.1f} more!')
