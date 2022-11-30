input_line = input()
word = ''
final_result = ''
special_c = 'c'
special_o = 'o'
special_n = 'n'
count_c = 0
count_o = 0
count_n = 0
is_met_c = False
is_met_o = False
is_met_n = False
while input_line != 'End':
    char = input_line
    if ord(char) >= 65 and ord(char) <= 90 or ord(char) >= 97 and ord(char) <= 122:
        
        if char == special_c:
            count_c += 1
            if count_c == 1:
                is_met_c = True
                char = ''
                            
        elif char == special_o:
            count_o += 1
            if count_o == 1:
                is_met_o = True
                char = ''
                            
        elif char == special_n:
            count_n += 1
            if count_n == 1:
                is_met_n = True
                char = ''
        
        word += char
            
        if  is_met_c and is_met_o and is_met_n:
            count_c = 0
            count_o = 0
            count_n = 0
            word += ' '
            is_met_c = False
            is_met_o = False
            is_met_n = False 
            
            final_result += word
            word = ''
                  
    input_line = input()
    #---------------------------------
print(final_result)