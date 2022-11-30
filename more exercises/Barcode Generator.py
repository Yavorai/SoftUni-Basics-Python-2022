from math import floor
start_num = int(input())
end_num = int(input())
result = ''

start_1 = floor((start_num / 1000) % 10)
start_2 = floor((start_num / 100) % 10)
start_3 = floor((start_num / 10) % 10)
start_4 = floor(start_num % 10)

end_1 = floor((end_num / 1000) % 10)
end_2 = floor((end_num / 100) % 10)
end_3 = floor((end_num / 10) % 10)
end_4 = floor(end_num % 10)

for a in range(start_1, end_1 + 1):
    if a % 2 != 0:
        for b in range(start_2, end_2 + 1):
            if b % 2 != 0:
                for c in range(start_3, end_3 + 1):
                    if c % 2 != 0:
                        for d in range(start_4, end_4 + 1):
                            if d % 2 != 0:
                                result += f'{a}{b}{c}{d} '

print(result)