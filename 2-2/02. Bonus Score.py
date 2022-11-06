num = int(input())
bonus = 0

if num > 1000:
    bonus += num * 0.1
elif num > 100:
    bonus += num * 0.2
else:
    bonus += 5
    
if num % 2 == 0:
    bonus += 1
    
if num % 10 == 5: # ако завършва на 5
    bonus += 2
    
print(bonus)
print(num + bonus)