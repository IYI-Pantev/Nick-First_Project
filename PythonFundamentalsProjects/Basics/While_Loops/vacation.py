needed_money = float(input())
owned_money = float(input())
days_count = 0
spending_days = 0
noSaving = False
enoughMoney = False
while True:
    action = input()
    current_sum = float(input())
    days_count += 1
    if action == 'spend':
        owned_money -= current_sum
        if owned_money < 0:
            owned_money = 0
        spending_days += 1
        if spending_days == 5:
            noSaving = True
            break
    elif action == 'save':
        owned_money += current_sum
        if owned_money >= needed_money:
            enoughMoney = True
            break
        spending_days = 0
if noSaving:
    print("You can't save the money.")
    print(f'{days_count}')
if enoughMoney:
    print(f'You saved the money for {days_count} days. ')
