moves_number = int(input())
int_1_9_count = 0
int_10_19_count = 0
int_20_29_count = 0
int_30_39_count = 0
int_40_50_count = 0
invalids_count = 0
result = 0
for i in range(moves_number):
    x = int(input())
    if x < 0 or x > 50:
        invalids_count += 1
        result /= 2
    elif 0 <= x <= 9:
        int_1_9_count += 1
        result += .2 * x
    elif 10 <= x <= 19:
        int_10_19_count += 1
        result += .3 * x
    elif 20 <= x <= 29:
        int_20_29_count += 1
        result += .4 * x
    elif 30 <= x <= 39:
        int_30_39_count += 1
        result += 50
    elif 40 <= x <= 50:
        int_40_50_count += 1
        result += 100

print(f"{result:.2f}")
print(f'From 0 to 9: {(int_1_9_count/moves_number*100):.2f}%')
print(f'From 10 to 19: {(int_10_19_count/moves_number*100):.2f}%')
print(f'From 20 to 29: {(int_20_29_count/moves_number*100):.2f}%')
print(f'From 30 to 39: {(int_30_39_count/moves_number*100):.2f}%')
print(f'From 40 to 50: {(int_40_50_count/moves_number*100):.2f}%')
print(f'Invalid numbers: {(invalids_count / moves_number * 100):.2f}%')

