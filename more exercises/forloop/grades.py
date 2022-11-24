students_count = int(input())
avg = 0
counter = 0
in_percent_top = 0
in_percent_4_499 = 0
in_percent_3_399 = 0
in_percent_3 = 0
number_1 = 0
number_2 = 0
number_3 = 0
number_4 = 0

for _ in range(1, students_count + 1):
    grade_of_student = float(input())
    
    
    if grade_of_student < 3:
        counter += 1
        number_1 += counter
        in_percent_3 = (number_1 * 100) / students_count
        
    elif grade_of_student >= 3 and grade_of_student <= 3.99:
        counter += 1
        number_2 += counter
        in_percent_3_399 = (number_2 * 100) / students_count
       
    elif grade_of_student >= 4 and grade_of_student <= 4.99:
        counter += 1
        number_3 += counter
        in_percent_4_499 = (number_3 * 100) / students_count
        
    elif grade_of_student >= 5:
        counter += 1
        number_4 += counter
        in_percent_top = (number_4 * 100) / students_count
        
        
    counter = 0
    avg += grade_of_student / students_count
    
    
print(f'Top students: {in_percent_top:.2f}%')
print(f'Between 4.00 and 4.99: {in_percent_4_499:.2f}%')
print(f'Between 3.00 and 3.99: {in_percent_3_399:.2f}%')
print(f'Fail: {in_percent_3:.2f}%')
print(f'Average: {avg:.2f}')