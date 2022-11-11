type_of_fuel = str(input())
tank_fuel_level = float(input())

if type_of_fuel == "Diesel" or type_of_fuel == "Gasoline" or type_of_fuel == "Gas":
    if tank_fuel_level >= 25: 
        print(f'You have enough {type_of_fuel.lower()}.')
    elif tank_fuel_level < 25: 
        print(f'Fill your tank with {type_of_fuel.lower()}!')
else:
    print('Invalid fuel!')




