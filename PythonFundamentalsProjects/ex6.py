kilos = int(input('Enter kilos: '))
height = int(input("Enter height: "))
bmi = kilos / (height / 100) ** 2
print(f'{bmi:.3f}')
if 18.5 <= bmi <= 24.9:
    print('you rock')
elif 25.9 <= bmi:
    print('more training, less eating')



