#fixed
nylon_protection_price_per_sqm = float(1.50)
paint_price_per_litter = float(14.50)
thinner_price_per_litter = float(5)
#extra expenses
more_paint_ten_percent = float(1.1)
extra_nylon = int(2)
bags_money_spend = float(0.40)
money_for_workers_per_hour = 0.30 
# input 
needed_nylon = int(input())
needed_paint = int(input())
amount_of_thinner = int(input())
hours_total_work = int(input())
#logic
total_cost_nylon =  (needed_nylon + extra_nylon) * nylon_protection_price_per_sqm
total_cost_paint =  (needed_paint * more_paint_ten_percent) * paint_price_per_litter
cost_thinner = amount_of_thinner * thinner_price_per_litter
total_sum_for_materials = total_cost_nylon + total_cost_paint + cost_thinner + bags_money_spend
total_money_for_workers = (total_sum_for_materials * money_for_workers_per_hour) * hours_total_work
final_sum = total_sum_for_materials + total_money_for_workers
print(final_sum)
#=========================================================================
'''price_nylon = 1.50
price_paint = 14.50
price_solvent = 5
factor_paint = 1.1
factor_nylon_add = 2
cost_bags = 0.40
factor_labor_per_hour = 0.30
qty_nylon = int(input())
qty_paint = int(input())
qty_solvent = int(input())
qty_labor = int(input())
cost_nylon = (qty_nylon + factor_nylon_add) * price_nylon
cost_paint = (qty_paint * factor_paint) * price_paint
cost_solvent = qty_solvent * price_solvent
cost_materials = cost_paint + cost_nylon + cost_solvent + cost_bags
price_labor = factor_labor_per_hour * cost_materials
cost_labor = price_labor * qty_labor
print(cost_materials + cost_labor)'''