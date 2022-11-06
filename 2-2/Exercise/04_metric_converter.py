# 1 meter (m)	1000 millimeters (mm)
# 1 meter (m)	100 centimeters (cm)
number = float(input())

incoming_metric = input()
outgoing_metric = input()

if incoming_metric == "mm":
    number /= 1000
elif incoming_metric == "cm":
    number /= 100

if outgoing_metric == "mm":
    number *= 1000
elif outgoing_metric == "cm":
    number *= 100

print(f"{number:.3f}")