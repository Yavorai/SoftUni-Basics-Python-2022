min_pass_grade = 4
fails_allowed = 1

student_name = input()
has_failed = False
has_graduated = False
school_year = 1
fail_count = 0
sum_grades = 0

while school_year < 13:
    grade = float(input())
    if grade >= min_pass_grade:
        # fail_count = 0
        sum_grades += grade
        if school_year == 12:
            has_graduated = True
        school_year += 1
        continue
    else:  # if grade < min_pass_grade:
        fail_count += 1
        if fail_count > fails_allowed:
            has_failed = True
            print(f'{student_name} has been excluded at {school_year} grade')
            break

if has_graduated and not has_failed:
    avg_grade = sum_grades / 12
    print(f'{student_name} graduated. Average grade: {avg_grade:.2f}')
