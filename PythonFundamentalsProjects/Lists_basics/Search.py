n = int(input())
word = input()

strings = []
filtered_list = []

for el in range(n):
    current_string = input()
    strings.append(current_string)
    if word in current_string:
        filtered_list.append(current_string)

print(strings)
print(filtered_list)
