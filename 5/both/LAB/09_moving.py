weidth = int(input())
lenght = int(input())
height = int(input())

room = weidth * lenght * height
count_box = 0

command = input()

while command != "Done":

    room -= int(command)

    if room <= 0:
        break

    command = input()

if room > 0:
    print(f"{room} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(room)} Cubic meters more.")