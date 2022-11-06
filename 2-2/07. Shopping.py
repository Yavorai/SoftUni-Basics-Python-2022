budget = float(input())
gpu_count = int(input())
cpu_count = int(input())
ram_count = int(input())

all_gpu = gpu_count * 250
cpu_price = all_gpu * 0.35
all_cpu = cpu_price * cpu_count
ram_price = all_gpu * 0.1
all_ram = ram_price * ram_count

total = all_gpu + all_cpu + all_ram

if gpu_count > cpu_count:
    total -= total * 0.15
    
if budget >= total:
    print(f'You have {budget - total:.2f} leva left!')
else:    
    print(f'Not enough money! You need {total - budget:.2f} leva more!')
    