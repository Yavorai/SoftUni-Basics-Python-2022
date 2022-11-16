bike_juniors = int(input())
bike_seniors = int(input())
road_type = input()

fee = 0
together = bike_juniors + bike_seniors

if road_type == 'trail':
    fee += (bike_seniors * 7) + (bike_juniors * 5.5)
elif road_type == 'cross-country':
    fee += (bike_seniors * 9.50) + (bike_juniors * 8)
    if together >= 50:
        fee = fee - fee * 0.25
elif road_type == 'downhill':
    fee += (bike_seniors * 13.75) + (bike_juniors * 12.25)
elif road_type == 'road':
    fee += (bike_seniors * 21.50) + (bike_juniors * 20)
    
fee = fee - fee * 0.05

print(f"{fee:.2f}")