command = input()
balance = 0

while command != 'NoMoreMoney':
    installment = float(command)

    if installment < 0:
        print('Invalid operation!')
        break
    balance += installment
    print(f'Balance increased with: {installment: .2f}lv.')

    command = input()

print(f'Balance total is: {balance: .2f}lv.')