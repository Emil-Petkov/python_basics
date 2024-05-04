target_steps = 10_000
total_steps = 0

while True:
    command = input()

    if command == 'Going home':
        steps_to_home = int(input())
        total_steps += steps_to_home

        if total_steps >= target_steps:
            print(f"Goal reached! Good job!")

            if total_steps > target_steps:
                print(f"{total_steps - target_steps} steps over the goal!")
        else:
            print(f"{target_steps - total_steps} more steps to reach goal.")
        break

    else:
        steps = int(command)
        total_steps += steps

        if total_steps >= target_steps:
            print("Goal reached! Good job!")

            if total_steps > target_steps:
                print(f"{total_steps - target_steps} steps over the goal!")
            break
