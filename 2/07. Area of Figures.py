import math
type_of_figure = str(input())

if type_of_figure == 'square':
    a = float(input())
    area = math.pow(a,2) 
    print(f"{area:.3f}")
elif type_of_figure == 'rectangle':
    a = float(input())
    b = float(input())
    area = a * b
    print(f"{area:.3f}")
elif type_of_figure == 'circle':
    r = float(input())
    area = math.pi * math.pow(r,2)
    print(f"{area:.3f}")
elif type_of_figure == 'triangle':
    a = float(input())
    b = float(input())
    area = (a * b) / 2
    print(f"{area:.3f}")