number = int(input())
for num in range(number +1): # започва от 0 
    if num % 2 == 0:
        print(2 ** num)  # вдигаме на втора степен 
        
#===========================================

n = int(input())
num = 1
for i in range(0, n +1, 2):
    print(num)
    num = num * 2 * 2