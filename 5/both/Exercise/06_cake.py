width = int(input())
length = int(input())

cake_pieces = width * length

while cake_pieces > 0:
    line = input()

    if line == "STOP":
        print(f'{cake_pieces} pieces are left.')
        break

    current_pieces = int(line)
    cake_pieces -= current_pieces

if cake_pieces <= 0:
    print(f'No more cake left! You need {abs(abs(cake_pieces))} pieces more.')





