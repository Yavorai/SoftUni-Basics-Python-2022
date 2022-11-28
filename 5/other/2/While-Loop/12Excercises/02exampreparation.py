# CONSTANTS
stop_word = 'Enough'
bad_grade_limit = 4
# VARIABLES
bad_grades_count = 0
grades_sum = 0
grades_count = 0
# INPUT
bad_grades_allowed = int(input())
task_name = input()
LastProblemName = ''

while task_name != stop_word:
    task_grade = int(input())
    grades_sum += task_grade
    grades_count += 1
    LastProblemName = task_name

    if task_grade <= bad_grade_limit:
        bad_grades_count += 1
    if bad_grades_count >= bad_grades_allowed:
        break
    task_name = input()

if task_name == stop_word:
    print(f'Average score: {(grades_sum / grades_count):.2f}')
    print(f'Number of problems: {grades_count}')
    print(f'Last problem: {LastProblemName}')
else:
    print(f'You need a break, {bad_grades_count} poor grades.')
