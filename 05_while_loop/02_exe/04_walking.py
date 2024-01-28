steps = input()

sum_steps = 0

while not steps == 'Going home':
    current_steps = int(steps)
    sum_steps += current_steps

    if sum_steps >= 10_000:
        print(f'Goal reached! Good job!\n{sum_steps - 10_000} steps over the goal!')
        break

    steps = input()

else:
    home_steps = int(input())
    sum_steps += home_steps

    if sum_steps >= 10_000:
        print(f'Goal reached! Good job!\n{abs(sum_steps - 10_000)} steps over the goal!')

    else:
        print(f'{10_000 - sum_steps} more steps to reach goal.')
