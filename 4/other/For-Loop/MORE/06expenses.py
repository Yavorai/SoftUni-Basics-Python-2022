water_monthly = 20
inet_monthly = 15
cost_others = 0
cost_electricity = 0

months_number = int(input())
cost_water = months_number * water_monthly
cost_inet = months_number * inet_monthly

for i in range(months_number):
    x = float(input())  # electricity for the month
    cost_electricity += x
    cost_others += (inet_monthly + water_monthly + x) * 1.2

total_cost = cost_electricity + cost_others + cost_water + cost_inet
avg_cost = total_cost / months_number

print(f"Electricity: {(cost_electricity):.2f} lv")
print(f"Water: {(cost_water):.2f} lv")
print(f"Internet: {(cost_inet):.2f} lv")
print(f"Other: {(cost_others):.2f} lv")
print(f"Average: {(avg_cost):.2f} lv")
