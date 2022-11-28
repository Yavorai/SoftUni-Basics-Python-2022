import sys
max_num = - sys.maxsize
data = input()

while data != 'Stop':
    number = int(data)
    if number > max_num:
        max_num = number
    data = input() 
print(max_num)   