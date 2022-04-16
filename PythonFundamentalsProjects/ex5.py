from unittest import result

# num = input()
# num_list = list(num)
# num_list.reverse()
# print(''.join(num_list))


num = input()

for i in range(len(num)-1, -1, -1):
    print(num[i], end='')
