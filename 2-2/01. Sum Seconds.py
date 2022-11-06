first = int(input())
second = int(input())
third = int(input())

total_time = first + second + third

minutes = total_time // 60 # целочислено делене без остатък да немерим секундите
seconds = total_time % 60 # връща остатъка от общите секунди

# с водеща нула
if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")
    
#=================================
# var 2
#  print(f"{minutes}:{seconds:02d}") означава че ако са по малко от две цифри ще го допълни с нула --> 02d, 03d, 04d etc...