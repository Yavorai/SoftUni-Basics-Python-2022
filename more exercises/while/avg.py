n = int(input())
sum_nums = 0
avg = 0
for _ in range(1, n + 1):
    curr_num = int(input())
    sum_nums += curr_num
    avg = sum_nums / n
print(f'{avg:.2f}')