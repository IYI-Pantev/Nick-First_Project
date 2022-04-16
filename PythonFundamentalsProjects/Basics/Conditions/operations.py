number_1 = int(input())
number_2 = int(input())
operator = input()


sum = 0

if operator == "+":
    sum = number_1 + number_2
    if sum % 2 == 0:
        print(f"{number_1} {operator} {number_2} = {sum} - {'even'}")
    else: print(f"{number_1} {operator} {number_2} = {sum} - {'odd'}")
elif operator == "-":
    sum = number_1 - number_2
    if sum % 2 == 0:
        print(f"{number_1} {operator} {number_2} = {sum} - {'even'}")
    else: print(f"{number_1} {operator} {number_2} = {sum} - {'odd'}")
elif operator == "*":
    sum = number_1 * number_2
    if sum % 2 == 0:
        print(f"{number_1} {operator} {number_2} = {sum} - {'even'}")
    else: print(f"{number_1} {operator} {number_2} = {sum} - {'odd'}")

if operator == '/':
    if not number_2 == 0:
        sum = number_1 / number_2
        print(f"{number_1} / {number_2} ={sum: .2f}")
    elif number_2 == 0:
        print(f'Cannot divide {number_1} by zero')

if operator == '%':
    if not number_2 == 0:
        sum = number_1 % number_2
        print(f"{number_1} % {number_2} = {number_1 % number_2}")
    else: print(f'Cannot divide {number_1} by zero')
