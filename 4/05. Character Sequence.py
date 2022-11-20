# range() е само за числа и индекси

'''text = 'This is SoftUni Python Basics.'
print(len(text))
letter = text[8]
print(letter)

for letter2 in text:
    if letter2 == 'S':
        break
    print(letter2)'''
    
#===========================================================
word = input()
for letter3 in word:
    print(letter3)
#===========================================================
   
word = input()
counter = 0

for letter4 in word:
    if letter4.upper() == letter4: # или с isupper()
        counter += 1
    print(counter)
    
#================================

word2 = input()
for index in range(0,len(word2)):
    print(word2[index])