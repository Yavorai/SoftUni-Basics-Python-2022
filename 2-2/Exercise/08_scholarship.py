import math
income = float(input())
average_grade = float(input())
minimum_salary = float(input())

social_scholarship = 0
grade_scholarship = 0

if average_grade > 4.50 and income < minimum_salary:
    social_scholarship = minimum_salary * 0.35

if average_grade >= 5.50:
    grade_scholarship = average_grade * 25

# print(social_scholarship)
# print (grade_scholarship)

if social_scholarship == 0 and grade_scholarship ==0:
    print("You cannot get a scholarship!")
elif social_scholarship != 0 and grade_scholarship == 0:
    print(f"You get a Social scholarship {math.floor(social_scholarship)} BGN")
elif social_scholarship == 0 and grade_scholarship != 0:
    print(f"You get a scholarship for excellent results {math.floor(grade_scholarship)} BGN")
else:
    if social_scholarship > grade_scholarship:
        print(f"You get a scholarship for excellent results {math.floor(grade_scholarship)} BGN")
    elif social_scholarship < grade_scholarship:
        print(f"You get a scholarship for excellent results {math.floor(grade_scholarship)} BGN")
    else:
        print(f"You get a scholarship for excellent results {math.floor(grade_scholarship)} BGN")

