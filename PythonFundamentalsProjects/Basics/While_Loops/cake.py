cake_width = int(input())
cake_length = int(input())

cake_square_area = cake_width*cake_length
holeCake = False
command = input()
total_pieces = 0
while command != 'STOP':
    cake_piece = int(command)
    total_pieces += cake_piece
    if cake_square_area - total_pieces <= 0:
        holeCake = True
        break
    command = input()

difference = abs(cake_square_area - total_pieces)
if holeCake:
    print(f"No more cake left!"
          f" You need {difference} pieces more.")
else:
    print(f"{difference} pieces are left.")



