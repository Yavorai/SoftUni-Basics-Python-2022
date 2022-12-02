max_limit_1_num = int(input()) # should be only even numbers
max_limit_2_num = int(input()) # only between 2 - 7 
max_limit_3_num = int(input()) # should be only even numbers

for first in range(2, max_limit_1_num + 1, 2):
    for second in range(2, max_limit_2_num + 1):
        for third in range(2, max_limit_3_num + 1, 2):
            if second == 2 or second == 3 or second == 5 or second == 7:
                print(f'{first} {second} {third}')
        
        
#=======================================
# max_n1 = int(input())
# max_n2 = int(input())
# max_n3 = int(input())

# for num1 in range(2, max_n1 + 1, 2):
#     for num2 in range(2, max_n2 + 1):
#         for num3 in range(2, max_n3 + 1, 2):
#             if num2 == 2 or num2 == 3 or num2 == 5 or num2 == 7:
#                 print(f"{num1} {num2} {num3}")