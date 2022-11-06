# read input
input_hour = int(input())
input_minutes = int(input())
# logic
all_minutes = input_hour * 60 + input_minutes
all_minutes += 15

hours = all_minutes // 60
minutes = all_minutes % 60
# output
if hours == 24:
    hours = 0

print(f"{hours}:{minutes:02d}")