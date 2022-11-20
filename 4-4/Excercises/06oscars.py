# Вход
# •	Име на актьора - текст
actor = input()
# •	Точки от академията - реално число в интервала [2.0... 450.5]
init_score = float(input())
# •	Брой оценяващи n - цяло число в интервала[1… 20]
count_judges = int(input())
score = init_score
max_score = 1250.5

# На следващите n-на брой реда:
# o	Име на оценяващия - текст
# o	Точки от оценяващия - реално число в интервала [1.0... 50.0]
for i in range(count_judges):
    judge_name = input()
    judge_score = float(input())
    x = len(judge_name) * judge_score / 2
    score += x

    if score > max_score:
        break

if score > max_score:
    print(f'Congratulations, {actor} got a nominee for leading role with {score:.1f}!')
else:
    print(f'Sorry, {actor} you need {(max_score - score):.1f} more!')
