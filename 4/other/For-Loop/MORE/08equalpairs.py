n_pairs = int(input())
max_diff = 0
sum_pair1 = 0
sum_pair2 = 0

for i in range(n_pairs):
    a = int(input())
    b = int(input())
    if i == 0:
        sum_pair1 = a + b
    sum_pair2 = a + b
    y = abs(sum_pair2 - sum_pair1)
    if y > max_diff:
        max_diff = y
    sum_pair1 = sum_pair2

if max_diff == 0:
    print(f'Yes, value={sum_pair2}')
else:
    print(f'No, maxdiff={max_diff}')
