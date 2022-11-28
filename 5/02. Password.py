username = input()
password = input()
data = input()
while password != data:
    data = input()
print(f'Welcome {username}!')
    

# var 2 
username = input()
user_password = input()
while True:
    data = input()
    if data == user_password:
        break
print(f'Welcome {username}!')

