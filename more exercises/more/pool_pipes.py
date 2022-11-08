pool_volume_litters = int(input())
p1_volume_hour = int(input())
p2_volume_hour = int(input())
hours_worker = float(input())

p1_total = p1_volume_hour * hours_worker
p2_total = p2_volume_hour * hours_worker

total_water_volume_in = p1_total + p2_total
pool_water_level_percent = (total_water_volume_in / pool_volume_litters) * 100

p1_how_much = total_water_volume_in - p2_total
p2_how_much = total_water_volume_in - p1_total

p1_in_percent = (p1_how_much / total_water_volume_in) * 100
p2_in_percent = (p2_how_much / total_water_volume_in) * 100

if total_water_volume_in > pool_volume_litters:
    print(f"For {hours_worker:.2f} hours the pool overflows with {(total_water_volume_in - pool_volume_litters):.2f} liters.")
else:
    print(f"The pool is {pool_water_level_percent:.2f}% full. Pipe 1: {p1_in_percent:.2f}%. Pipe 2: {p2_in_percent:.2f}%.")