import sys
min_num = sys.maxsize
data = input()

while data != 'Stop':
    number = int(data)
    if number < min_num:
        min_num = number
    data = input()
print(min_num)