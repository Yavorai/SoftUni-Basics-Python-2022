stop_word = 'End'
word = ''
text = ''
skip_letter_1 = 'c'  # *2
skip_letter_2 = 'o'  # *3
skip_letter_3 = 'n'  # *5
command_value = 1
skip1 = 2
skip2 = 3
skip3 = 5

letter = input()
while letter != stop_word:
    # if letter.isalpha():  #  replace by check for latin letters only
    if 90 >= ord(letter) >= 65 or 122 >= ord(letter) >= 97:  # check for latin letters only
        if letter == skip_letter_1:
            if command_value % skip1 != 0:
                command_value *= skip1
                letter = ''
        elif letter == skip_letter_2:
            if command_value % skip2 != 0:
                command_value *= skip2
                letter = ''
        elif letter == skip_letter_3:
            if command_value % skip3 != 0:
                command_value *= skip3
                letter = ''

        word = word + letter

        if command_value == skip1 * skip2 * skip3:
            word = word + ' '
            text = text + word
            print(word, end='')
            command_value = 1
            word = ''
    letter = input()
# print()
# print(text)
