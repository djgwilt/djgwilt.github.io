file = open("day 5/input 5.txt","r")
seeds = [432986705, 28073546, 1364097901, 88338513, 2733524843, 234912494, 3151642679, 224376393, 485709676, 344068331, 1560394266, 911616092, 3819746175, 87998136, 892394515, 435690182, 4218056486, 23868437, 848725444, 8940450]
map1 = []
map2 = []
map3 = []
map4 = []
map5 = []
map6 = []
map7 = []
map = 1
for line in file:
    if map > 7:
        break
    line = line.strip()
    line = line.split(" ")
    if line != ".":
        if map == 1:
            map1.append(line)
        elif map == 2:
            map2.append(line)
        elif map == 3:
            map3.append(line)
        elif map == 4:
            map4.append(line)
        elif map == 5:
            map5.append(line)
        elif map == 6:
            map6.append(line)
        elif map == 7:
            map7.append(line)
    else:
        map += 1


for seed in seeds:
    if True:
        print("hi")