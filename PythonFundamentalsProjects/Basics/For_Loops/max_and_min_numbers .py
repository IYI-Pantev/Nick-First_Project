import sys
n = int(input("how many numbers you'll compare: "))
max = -sys.maxsize
min = sys.maxsize

for i in range(n):
    number = int(input())
    if number < min:
        min = number

    if number > max:
        max = number

print(f'Max number: {max}')
print(f'Min number: {min}')
