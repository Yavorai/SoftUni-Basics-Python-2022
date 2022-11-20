count_tournaments = int(input())
init_scores = int(input())
scores = init_scores
won_tournaments = 0
for i in range(count_tournaments):
    finish = input()
    if finish == 'W':
        scores += 2000
        won_tournaments += 1
    elif finish == 'F':
        scores += 1200
    elif finish == 'SF':
        scores += 720

print(f'Final points: {scores}')
print(f'Average points: {int((scores-init_scores) / count_tournaments)}')
print(f'{(won_tournaments / count_tournaments * 100):.2f}%')
