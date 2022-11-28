bad_grades = int(input())

failed_times = 0
solved_problems_count = 0
sum_grades = 0
last_problem = ' '
is_he_fail = True

while failed_times < bad_grades:
    problem_name = input()
    if problem_name == "Enough":
        is_he_fail = False
        break

    grade = int(input())
    if grade <= 4:
        failed_times += 1
    sum_grades += grade
    solved_problems_count += 1
    last_problem = problem_name

if is_he_fail:
    print(f'You need a break, {bad_grades} poor grades.')
else:
    print(f'Average score: {sum_grades / solved_problems_count:.2f}')
    print(f'Number of problems: {solved_problems_count}')
    print(f'Last problem: {last_problem}')

