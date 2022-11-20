import sys
 
n = int(input())
 
max_num = -sys.maxsize
total_sum = 0
for i in range(1, n + 1):
    current_num = int(input())
 
    total_sum = total_sum + current_num
 
    if current_num > max_num:
        max_num = current_num
 
other_sum_num = total_sum - max_num
 
if max_num == other_sum_num:
    print("Yes")
    print(f"Sum = {other_sum_num}")
else:
    print("No")
    diff = abs(other_sum_num - max_num)
    print(f"Diff = {diff}")