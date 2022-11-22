period = int(input())
doctors = 7
patients_ok = 0
patients_not = 0

for i in range(1, period + 1):
    
    if i % 3 == 0 and patients_not > patients_ok:
        doctors += 1
        
    patients = int(input())
            
    if patients <= doctors:
        patients_ok += patients
    elif patients > doctors:
        patients_ok += doctors
        patients_not += abs(patients - doctors)
        
        
print(f'Treated patients: {patients_ok}.')
print(f'Untreated patients: {patients_not}.')