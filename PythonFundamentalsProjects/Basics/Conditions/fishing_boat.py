budged = int(input())
season = input()
number_of_fishermen = int(input())

rental_price = 0

if season == 'Summer' or season == 'Autumn':
    rental_price = 4200
elif season == 'Spring':
    rental_price = 3000
elif season == 'Winter':
    rental_price = 2600
# следват отстъпки
if 1 <= number_of_fishermen <= 6:
    rental_price *= 0.90
elif 7 <= number_of_fishermen <= 11:
    rental_price *= 0.85
elif number_of_fishermen >= 12:
    rental_price *= 0.75


if number_of_fishermen % 2 == 0:
    if not season == 'Autumn':
        rental_price *= 0.95

if (budged - rental_price) >= 0:
    print(f"Yes! You have{(budged - rental_price): .2f} leva left.")
if (budged - rental_price) < 0:
    print(f'Not enough money! You need{abs(budged - rental_price): .2f} leva.')

