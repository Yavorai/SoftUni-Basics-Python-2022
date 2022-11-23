loads_number = int(input())

price = 0
sum_tons = 0
avg_price_per_ton = 0
van_percent = 0
truck_percent = 0
train_percent = 0

for load in range(1, loads_number + 1):
    curr_ton = int(input())
    
    if curr_ton <= 3:
        price += curr_ton * 200
        sum_tons += curr_ton
        van_percent += curr_ton
    elif curr_ton >= 4 and curr_ton <= 11:
        price += curr_ton * 175
        sum_tons += curr_ton
        truck_percent += curr_ton
    elif curr_ton >= 12:
        price += curr_ton * 120
        sum_tons += curr_ton
        train_percent += curr_ton
        
    avg_price_per_ton = price / sum_tons
    
print(f'{avg_price_per_ton:.2f}')   
print(f'{van_percent/sum_tons*100:.2f}%')   
print(f'{truck_percent/sum_tons*100:.2f}%')   
print(f'{train_percent/sum_tons*100:.2f}%')   