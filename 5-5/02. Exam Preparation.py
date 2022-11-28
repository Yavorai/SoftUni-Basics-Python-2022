number_poor_grades = int(input())
 
flag = False
input_line = input()
sum_grades = 0
count_grades = 0
last_problem = ""
poor_count_grades = 0
while input_line != "Enough":
    problem_name = input_line
    current_grade = int(input())
 
    if current_grade <= 4:
        poor_count_grades += 1
 
    if poor_count_grades >= number_poor_grades:
        flag = True
        break
 
    count_grades = count_grades + 1
    sum_grades = sum_grades + current_grade
    last_problem = input_line
 
    input_line = input()
 
if flag:
    print(f"You need a break, {poor_count_grades} poor grades.")
else:
    avg_grade = sum_grades / count_grades
    print(f"Average score: {avg_grade:.2f}")
    print(f"Number of problems: {count_grades}")
    print(f"Last problem: {last_problem}")
 