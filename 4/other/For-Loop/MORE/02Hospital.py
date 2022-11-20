period_days = int(input())
doctros_number = 7
priod_check_numbers = 3  # each third day
treated_patients_number = 0
untreated_patients_number = 0

for i in range(1, period_days + 1):
    x = int(input())  # patients_for_the_day
    if i % 3 == 0:
        if untreated_patients_number > treated_patients_number:
            doctros_number += 1
    if x > doctros_number:
        untreated_patients_number += (x - doctros_number)
        treated_patients_number += doctros_number
    else:
        treated_patients_number += x

print(f"Treated patients: {treated_patients_number}.")
print(f"Untreated patients: {untreated_patients_number}.")
