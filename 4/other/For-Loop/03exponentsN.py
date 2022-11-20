n = int(input())
b = 1  # for version 2
for i in range(0, n + 1, 2):
    print(2 ** i)
# version 2:
#     print(f'{2 ** i} {b}')
#     b = b * 2 * 2
