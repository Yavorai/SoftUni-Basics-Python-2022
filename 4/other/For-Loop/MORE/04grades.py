n_students = int(input())
grade = 0
st_top_above_5 = 0
st_4to5 = 0
st_3to4 = 0
st_fail_less_3 = 0
sum_grades = 0

for i in range(n_students):
    grade = float(input())
    sum_grades += grade
    if grade >= 5:
        st_top_above_5 += 1
    elif 4 <= grade < 5:
        st_4to5 += 1
    elif 3 <= grade < 4:
        st_3to4 += 1
    elif grade < 3:
        st_fail_less_3 += 1

# Да се отпечатат на конзолата 5 реда, които съдържат следната информация:
# Ред 1 -	"Top students: {процент студенти с успех 5.00 или повече}%"
print(f'Top students: {(st_top_above_5 / n_students * 100):.2f}%')
# Ред 2 -	"Between 4.00 and 4.99: {между 4.00 и 4.99 включително}%"
print(f'Between 4.00 and 4.99: {(st_4to5 / n_students * 100):.2f}%')
# Ред 3 -	"Between 3.00 and 3.99: {между 3.00 и 3.99 включително}%"
print(f'Between 3.00 and 3.99: {(st_3to4 / n_students * 100):.2f}%')
# Ред 4 -	"Fail: {по-малко от 3.00}%"
print(f'Fail: {(st_fail_less_3 / n_students * 100):.2f}%')
# Ред 5 -	"Average: {среден успех}"
print(f'Average: {(sum_grades / n_students):.2f}')
# Всички числа трябва да са форматирани до вторият знак след десетичната запетая.
