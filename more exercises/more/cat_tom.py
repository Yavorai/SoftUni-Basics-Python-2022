days_off = int(input())

tom_limit = 30000
year = 365
playtime_working_days = 63  # min
playtime_days_off = 127  # min

working_days = year - days_off

total_play_working_days = working_days * playtime_working_days
total_play_days_off = days_off * playtime_days_off
total_play_time = total_play_working_days + total_play_days_off

if tom_limit < total_play_time:
    difference = total_play_time - tom_limit
    h = int(difference / 60)
    m = int(difference % 60)
    print('Tom will run away')
    print(f"{h} hours and {m} minutes more for play")
elif tom_limit > total_play_time:
    difference = tom_limit - total_play_time
    h = int(difference / 60)
    m = int(difference % 60)
    print('Tom sleeps well')
    print(f'{h} hours and {m} minutes less for play')
