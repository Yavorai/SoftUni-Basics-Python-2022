goal = 10000
total_steps = 0
stop_word = 'Going home'
steps = 0
last_loop = False
while total_steps < goal:
    x = input()
    if x == stop_word:
        last_loop = True
        continue
    steps = int(x)
    total_steps += steps
    if last_loop:
        break
diff = abs(total_steps - goal)
if total_steps < goal:
    print(f'{diff} more steps to reach goal.')
else:
    print(f'Goal reached! Good job!')
    print(f'{diff} steps over the goal!')
