trip_km = int(input())
day_or_night = str(input())

taxi_starting_fee = 0.70
taxi_day_km = 0.79
taxi_night_km = 0.90
bus_day_and_night_fee = 0.09    # min 20 km
train_day_and_night_fee = 0.06  # min 100 km

total_price = 0

if trip_km >= 100:
    total_price = trip_km * train_day_and_night_fee    
elif trip_km >= 20:
    total_price = trip_km * bus_day_and_night_fee
else:
    if day_or_night == 'day':
        total_price = trip_km * taxi_day_km + taxi_starting_fee
    elif day_or_night == 'night':
        total_price = trip_km * taxi_night_km + taxi_starting_fee
        
print(f'{total_price:.2f}')