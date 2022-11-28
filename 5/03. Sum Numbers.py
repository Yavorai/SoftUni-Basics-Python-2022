constant_number = int(input())
sum_nums_counter = 0

while True:
    curr_nums = int(input())
    sum_nums_counter += curr_nums
    
    if sum_nums_counter >= constant_number:
        print(sum_nums_counter)
        break