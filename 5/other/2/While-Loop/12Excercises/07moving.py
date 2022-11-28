space_width = int(input())
space_length = int(input())
space_height = int(input())
box_size = 1 * 1 * 1
boxes_to_fit = int((space_width * space_length * space_height) / box_size)
space_is_over = False
x = input()
while x != 'Done':
    boxes_moved_in = int(x)
    boxes_to_fit -= boxes_moved_in
    if boxes_to_fit <= 0:
        space_is_over = True
        break
    x = input()

if space_is_over:
    print(f'No more free space! You need {abs(boxes_to_fit)} Cubic meters more.')
else:
    print(f'{boxes_to_fit} Cubic meters left.')
