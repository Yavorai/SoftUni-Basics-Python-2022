a = 1
while a < 6: # while true булево условие --> true or false
    print(a)
    a += 1
#=====================
while True:   # or username != 'End'
    username = input() 
    if username == 'End':
        print('End of while Loop!')
        break
    print(f'Hello {username}...')
#=======================
counter = 0
while True:
    if counter == 3:
        print(f'Counter of repeating - {counter}')
        break
    print('Hello world!')
    counter += 1
#=======================
a = 1
while a < 6:
    a += 1
    if a == 3:
        continue
    print(a)