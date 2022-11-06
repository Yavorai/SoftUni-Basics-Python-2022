import math
world_record_seconds = float(input())
distance = float(input())
seconds_for_meter = float(input())

distance_Ivan = distance * seconds_for_meter
delay = math.floor(distance / 15) * 12.5
total_time = distance_Ivan + delay

if world_record_seconds < total_time:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {total_time - world_record_seconds:.2f} seconds slower.")
