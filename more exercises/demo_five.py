from math import floor

w_from_m_to_cm = float(input()) * 100 
h_from_m_to_cm = float(input()) * 100 - 100 # - коридора

h_desk_size = 70
w_desk_size = 120

number_of_desks_h = floor(h_from_m_to_cm / h_desk_size)
number_of_desks_w = floor(w_from_m_to_cm / w_desk_size)

all_workspaces = (number_of_desks_h * number_of_desks_w) - 3
print(all_workspaces)