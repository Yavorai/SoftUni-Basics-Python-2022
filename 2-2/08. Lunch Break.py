from math import ceil

movie_name = input()
movie_duration = int(input())
break_time = int(input())

lunch_break = break_time / 8
relax_break = break_time / 4

free_time = break_time - (lunch_break + relax_break) 

if free_time >= movie_duration:
    print(f'You have enough time to watch {movie_name} and left with {ceil(free_time - movie_duration)} minutes free time.')
else:    
    print(f'You don\'t have enough time to watch {movie_name}, you need {ceil(movie_duration - free_time)} more minutes.')