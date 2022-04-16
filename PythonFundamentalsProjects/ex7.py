rows = int(input())
if rows <= 0:
    print('Error')

cols = int(input())
if cols > 30:
    print('Error')

for i in range(rows):
    for j in range(cols):
        print('#', end='  ')
    print()

'''
асдсдфасгасдфасдгасдас
асдсдфасгасдфасдгасдасасд
асдсдфасгасдфасдгасдас
'''