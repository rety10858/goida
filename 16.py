import random as rm
name = ["Роза", "Ландыш", "Подорожник"]
colors = ["Черний", "Бели", "Красни", "Сини"]
b = list(colors[rm.randint(0, 3)] for x in range(0, len(name)))
a = dict(zip(name, b))
print(a)