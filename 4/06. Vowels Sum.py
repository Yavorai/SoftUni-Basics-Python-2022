text = input()
obj = {
    "a": 1,
    "e": 2,
    "i": 3,
    "o": 4,
    "u": 5,
}
sum_chars = 0
for index in range(0, len(text)):
    char = text[index]
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        sum_chars += int(obj[char])
print(sum_chars)
