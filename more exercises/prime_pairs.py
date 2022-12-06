first_pair = int(input())
second_pair = int(input())
diff_first_pair = int(input())
diff_second_pair = int(input())
max_range_first = first_pair + diff_first_pair
max_range_second = second_pair + diff_second_pair

for a in range(first_pair, max_range_first + 1):
    for b in range(second_pair, max_range_second + 1):
        
        isPrime = True
        isPrime2 = True
        
           
        for k in range(2, a):   
            if a % k == 0:
                isPrime2 = False    
                break 
        
        
        for k in range(2, b):
            if b % k == 0:
               isPrime = False
               break 
          
           
        if isPrime and isPrime2:
            print(f'{a}{b}')