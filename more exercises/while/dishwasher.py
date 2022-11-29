bottles_number = int(input())
dishes_qty = 0
pots = 0
plates = 0
counter = 0
used_detergent = 0
detergent_qty = bottles_number * 750
isFinished = False

data = input()
while data != 'End':
    counter += 1
    dishes_number = int(data)
    
    if counter % 3 == 0:
        dishes_qty = dishes_number * 15
        pots += dishes_number
        
    else:
        dishes_qty = dishes_number * 5
        plates += dishes_number
        
    used_detergent += dishes_qty 
    detergent_qty -= dishes_qty
    
    if detergent_qty < 0:
        isFinished = True
        print(f'Not enough detergent, {abs(detergent_qty)} ml. more necessary!')
        break
    
    data = input()  
      
if isFinished == False:
    print('Detergent was enough!')
    print(f'{plates} dishes and {pots} pots were washed.')
    print(f'Leftover detergent {detergent_qty} ml.')
