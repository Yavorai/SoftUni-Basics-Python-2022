cake_width = int(input())
cake_length = int(input())
piece_size = 1 * 1
pieces_of_cake = int((cake_width * cake_length) / piece_size)
cake_is_over = False
x = input()
while x != 'STOP':
    pieces_taken = int(x)
    pieces_of_cake -= pieces_taken
    if pieces_of_cake <= 0:
        cake_is_over = True
        break
    x = input()

if cake_is_over:
    print(f'No more cake left! You need {abs(pieces_of_cake)} pieces more.')
else:
    print(f'{pieces_of_cake} pieces are left.')
