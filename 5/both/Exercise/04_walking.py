goal = 10000

count_steps = 0

while count_steps < goal:
    line = input()
    if line == "Going home":
        steps_home = int(input())
        count_steps += steps_home
        if count_steps < goal:
            diff = goal - count_steps
            print(f'{diff} more steps to reach goal.')
        break

    steps = int(line)
    count_steps += steps

    if count_steps > goal:
        break

if count_steps >= goal:
    print('Goal reached! Good job!')
    print(f'{count_steps - goal} steps over the goal!')



