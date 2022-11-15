budget = float(input())
ticket_type = input()
people_in_group = int(input())
vip = 499.99
normal = 249.99
money_for_tickets = 0


if people_in_group >= 1 and people_in_group <= 4:
    budget =  budget - budget * 0.75
    if ticket_type == 'VIP':
        money_for_tickets = vip * people_in_group
    elif ticket_type == 'Normal':
        money_for_tickets = normal * people_in_group

elif people_in_group >= 5 and people_in_group <= 9:
    budget =  budget - budget * 0.60

    if ticket_type == 'VIP':
        money_for_tickets = vip * people_in_group
    elif ticket_type == 'Normal':
        money_for_tickets = normal * people_in_group

elif people_in_group >= 10 and people_in_group <= 24:
    budget =  budget - budget * 0.50

    if ticket_type == 'VIP':
        money_for_tickets = vip * people_in_group
    elif ticket_type == 'Normal':
        money_for_tickets = normal * people_in_group

elif people_in_group >= 25 and people_in_group <= 49:
    budget =  budget - budget * 0.40

    if ticket_type == 'VIP':
        money_for_tickets = vip * people_in_group
    elif ticket_type == 'Normal':
        money_for_tickets = normal * people_in_group

elif people_in_group >= 50:
    budget =  budget - budget * 0.25

    if ticket_type == 'VIP':
        money_for_tickets = vip * people_in_group
    elif ticket_type == 'Normal':
        money_for_tickets = normal * people_in_group




if money_for_tickets > budget:
    print(f"Not enough money! You need {money_for_tickets - budget:.2f} leva.")
elif budget >= money_for_tickets:
    print(f"Yes! You have {budget - money_for_tickets:.2f} leva left.")