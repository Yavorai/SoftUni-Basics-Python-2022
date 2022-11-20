number = int(input())
total_sum = 0
for _ in range(number): # _ долна черта е когато няма да ползваме променлива -->> добра практика в пайтън!!!
    current_num = int(input())
    total_sum += current_num 

print(total_sum)


#==================================

for num in range(1,11):
    #if num == 5: # if num % 2 == 0 --> even
        #break # continue
    print(num)

else:
    print('End of loop')