n = int(input())
 
p_1_count = 0
p_2_count = 0
p_3_count = 0
p_4_count = 0
p_5_count = 0
for i in range(1, n + 1):
    current_num = int(input())
 
    if current_num < 200:
        p_1_count = p_1_count + 1
    elif current_num <= 399:
        p_2_count = p_2_count + 1
    elif current_num <= 599:
        p_3_count = p_3_count + 1
    elif current_num <= 799:
        p_4_count = p_4_count + 1
    elif current_num >= 800:
        p_5_count = p_5_count + 1
 
percent_p_1 = p_1_count / n * 100
print(f"{percent_p_1:.2f}%")
percent_p_2 = p_2_count / n * 100
print(f"{percent_p_2:.2f}%")
percent_p_3 = p_3_count / n * 100
print(f"{percent_p_3:.2f}%")
percent_p_4 = p_4_count / n * 100
print(f"{percent_p_4:.2f}%")
percent_p_5 = p_5_count / n * 100
print(f"{percent_p_5:.2f}%")