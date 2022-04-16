budget = float(input())
season = input()
destination = " "   # Bulgaria, Balkans, Europe
facility = " "   # Camp or Hotel
expenditure = 0.0

if season == "summer" and destination != 'Europe':
    facility = "Camp"
else:
    facility = 'Hotel'

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        expenditure = budget*0.3
    elif season == 'winter':
        expenditure = budget*0.7
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        expenditure = budget*0.4
    elif season == 'winter':
        expenditure = budget*0.8
else:
    destination = 'Europe'
    expenditure = budget*0.9

print(f"Somewhere in {destination}" )
print(f"{facility} -{expenditure: .2f}")

