username = input()
password = input()
str_pass = input()  # password+'!!!'
while str_pass != password:
    str_pass = input()
if str_pass == password:
    print(f'Welcome {username}!')
