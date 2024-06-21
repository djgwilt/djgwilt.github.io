file = open("day 1/input 1.txt" , "r")
total = 0
for line in file:
    x = 0
    y = False
    line = line.strip()
    line = list(str(line))
    while y == False:
        if line[x].isdigit() == True:
            total += int(line[x]) * 10
            y = True
        x += 1
    y = False
    x = -1
    while y == False:
        if line[x].isdigit() == True:
            total += int(line[x])
            y = True
        x = x - 1

print(total)

file = open("day 1/input 1.txt" , "r")
total = 0
for line in file:
    for charachter in line:
        if charachter.isdigit() == True:
            total += int(charachter) * 10
            break
    for charachter in line:
        if charachter.isdigit() == True:
            lastdigit = int(charachter)
    total += lastdigit
    
print(total)