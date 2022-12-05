max_limit_1_num = int(input())
max_limit_2_num = int(input()) 
max_limit_3_num = int(input()) 
for first in range(2, max_limit_1_num + 1, 2):
    for second in range(2, max_limit_2_num + 1):
        for third in range(2, max_limit_3_num + 1, 2):
            count = 0
            for i in range(1, max_limit_2_num + 1):
                if second % i == 0:
                    count += 1
            if count == 2:
                print(f'{first} {second} {third}')