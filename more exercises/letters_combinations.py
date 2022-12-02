for_start_letter = input()
for_end_letter = input()
to_skip_letter = input()
start_char = ord(for_start_letter)
end_char = ord(for_end_letter)
to_skip_char = ord(to_skip_letter)

counter = 0

for one in range(start_char, end_char + 1):
    for two in range(start_char, end_char + 1):
        for three in range(start_char, end_char + 1):
            if one == to_skip_char or two == to_skip_char or three == to_skip_char:
                continue
            else:
                counter += 1
                print(f'{chr(one)}{chr(two)}{chr(three)} ',end='')
print(counter)