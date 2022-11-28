# var 1
word = input()
while word != 'Stop':
    print(word)
    word = input()


# var 2 --> по добър вариант
while True:
    word = input()
    if word == 'Stop':
        break
    print(word)