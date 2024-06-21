file = open("day 10/input.txt","r")

array = []
count = 0 

for line in file:
    line = line.strip()
    array.append([])
    for i in line:
        array[count].append(i)
    count += 1

y = 0

for line in array:
    x = 0
    for i in line:
        if i == "S":
            print(f"({x},{y})")
            sx = x +1
            sy = y -1
            break
        x += 1
    y += 1

print(array[sx][sy])

if array[sx+1][sy] == "|" or array[sx][sy+1] == "J" or array[sx][sy+1] == "L":
    fx = sx
    fy = sy + 1 
    enter = "u"
elif array[sx-1][sy] == "|" or array[sx-1][sy] == "F" or array[sx-1][sy] == "7":
    fx = sx
    fy = sy - 1
    enter = "d"
elif array[sx][sy+1] == "-" or array[sx][sy+1] == "7" or array[sx][sy+1] == "J":
    fx = sx + 1
    fy = sy
    enter = "r"

total = 0
while array[fx][fy] != "S":
    total += 1
    if array[fx][fy] == "-":
        if enter == "r":
            fy -= 1
        else:
            fy += 1
    elif array[fx][fy] == "|":
        if enter == "u":
            fx += 1
        else:
            fx -= 1
    elif array[fx][fy] == "F":
        if enter == "d":
            fy += 1
            enter = "l"
        else:
            fx += 1
            enter = "u"
    elif array[fx][fy] == "J":
        if enter == "u":
            fy -= 1
            enter = "r"
        else:
            fx -= 1
            enter = "d"
    elif array[fx][fy] == "7":
        if enter == "l":
            fx += 1
            enter = "u"
        else:
            fy -= 1
            enter = "r"
    elif array[fx][fy] == "L":
        if enter == "u":
            fy +=1
            enter = "l"
        else:
            fx -= 1
            enter = "d"
print(total)