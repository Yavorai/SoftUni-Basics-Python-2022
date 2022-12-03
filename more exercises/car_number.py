num_1 = int(input())
num_2 = int(input())
result = ''

for a in range(num_1, num_2 + 1):
    for b in range(num_1, num_2 + 1):
        for c in range(num_1, num_2 + 1):
            for d in range(num_1, num_2 + 1):
                if a > d and (b + c) % 2 == 0:
                    if a % 2 == 0 and d % 2 != 0:
                        result += f'{a}{b}{c}{d} '
                    elif (a % 2 != 0) and d % 2 == 0:
                        result += f'{a}{b}{c}{d} '
                        
    
print(result)

