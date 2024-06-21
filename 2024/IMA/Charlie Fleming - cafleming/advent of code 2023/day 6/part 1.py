races = [[51,222],[92,2031],[68,1126],[90,1225]]

total = 0
for race in races:
    winning = 0
    for speed in range(int(race[0])):
        time = int(race[0]) - speed
        distance = speed * time
        if distance > race[1]:
            winning += 1
    if total == 0:
        total = winning
    else:
        total = total * winning

print(total)
    