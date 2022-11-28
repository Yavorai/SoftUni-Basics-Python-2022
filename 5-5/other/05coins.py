# coin01=.01
# coin02 = .02
# coin03 = .05
# coin04 = .1
coins_list = [2, 1, .5, .2, .1, .05, .02, .01]
coins_count = 0
# print(len(coins_list))
# print(coins_list[0])
sum_change = float(input())

for coin in coins_list:
    num = int(round(sum_change, 2) // coin)
    coins_count += num
    sum_change -= round(num * coin, 2)
    if sum_change == 0:
        break

print(int(coins_count))
