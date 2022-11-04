
price_skumria_kg = float(input())
price_tsatsa_kg = float(input())

palamud_kg = float(input())
safrid_kg = float(input()) 
midi_kg = float(input()) # 7.50 lv per kg

price_palamud = price_skumria_kg + price_skumria_kg * 0.60

price_safrid = price_tsatsa_kg + price_tsatsa_kg * 0.80
total_price_safrid = safrid_kg * price_safrid
total_price_palamud = price_palamud * palamud_kg

price_midi = midi_kg * 7.50

sum_total = total_price_safrid + price_midi + total_price_palamud 


print(format(sum_total,".2f"))