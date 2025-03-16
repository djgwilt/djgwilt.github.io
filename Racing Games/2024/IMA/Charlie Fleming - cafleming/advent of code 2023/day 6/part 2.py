races = [51926890,222203111261225]

winning = 0
for speed in range(int(races[0])):
    time = int(races[0]) - speed
    distance = speed * time
    if distance > races[1]:
        winning += 1

print(winning)