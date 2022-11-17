import sys
while True:
    n = int(input('Height: '))
    if n > 0:  # за да не се въвеждат негативни числа
        break
for i in range(n):
    print('#')

# ===================================================


def main():
    height = get_height()
    for i in range(height):
        print('#')

def get_height():
    while True:
        try:
            n = int(input('Height: '))
            if n > 0:
                return n
        except ValueError:
            print('not an integer')

# ==================================================


for i in range(4):
    # с едн и нещо можем да кажем как да ги принтира, как да завършват --->>> нещо като .join in js
    print('?', end='\n')
    print('?' * 4)

for i in range(3):
    for j in range(3):
        print('#', end='')
    print()
for i in range(3):
    print('#' * 3)

# ==================================================

scores = [72, 73, 33]
average = sum(scores) / len(scores)
print(f'Average: {average}')


scores = []
for i in range(3):
    score = get_int('Score: ')
    scores.append(score)  # or scores += [score]
average = sum(scores) / len(scores)
print(f'Average: {average}')

# =================================================
names = ['Bill', 'Charlie', 'Pesho', 'Gosho', 'Stamat']

name = input('Name: ')
if name in names:
    print('Found')
    sys.exit(0)
print('Not found')
sys.exit(1)

# =====================================================

# dictionary == object in js

people = {
    "pesho": '321312313',
    'gosho': '32321333333333',
}
name = input()
if name in people:
    tel_number = people[name]
    print(f'Number: {tel_number}')
