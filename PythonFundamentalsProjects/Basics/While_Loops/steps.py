target_steps = 10000
total_steps = 0
command = input()
goalReached = False

while command != 'Going home':
    current_steps = int(command)
    total_steps += current_steps
    if total_steps >= target_steps:
        goalReached = True
        break
    command = input()
if command == 'Going home':
    last_steps = int(input())
    total_steps += last_steps
    if total_steps >= target_steps:
        goalReached = True

difference = abs(target_steps-total_steps)
if goalReached:
    print('Goal reached! Good job!')
    print(f'{difference} steps over the goal!')
else:
    print(f'{difference} more steps to reach goal.')
