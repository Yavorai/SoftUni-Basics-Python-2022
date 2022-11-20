in_text = input()
vowel_sum = 0
for char in in_text:
    x=char.lower()
    if x == 'a':
        vowel_sum += 1
    elif x == 'e':
        vowel_sum += 2
    elif x == 'i':
        vowel_sum += 3
    elif x == 'o':
        vowel_sum += 4
    elif x == 'u':
        vowel_sum += 5

print(vowel_sum)
