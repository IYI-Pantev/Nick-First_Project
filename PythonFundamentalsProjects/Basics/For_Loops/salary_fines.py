tabs = int(input())
salary = float(input())

for i in range(tabs):
    websites = input()
    if websites == 'Facebook':
        salary -= 150
    if websites == 'Instagram':
        salary -= 100
    if websites == 'Reddit':
        salary -= 50
    if salary <= 0:
        print('You have lost your salary.')
        break


if salary > 0:
    print(int(salary))


