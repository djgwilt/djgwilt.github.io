file = open("day 2/input 2.txt" , "r")
total = 0
for line in file:
    x = 0
    valid = True
    line = line.strip()
    line = line.replace(";",",")
    y = line.split(":")
    z = y[1].split(" ")
    for word in z:
        if word.isdigit() == True:
            if int(word) > 14:
                x = 1
            elif int(word) > 13:
                x = 2
            elif int(word) > 12:
                x = 3
        else:
            if x == 1:
                valid = False
                break
            if x == 2:
                if word == "green,":
                    valid = False
                    break
            if x == 3:
                if word == "red,":
                    valid = False
                    break
    if valid == False:
        y = y[0].split(" ")
        total += int(y[1])
print(total)






file = open("day 2/input 2.txt" , "r")
total = 0
for line in file:
    valid = True
    x = 0
    line = line.strip()
    line = line.replace(";",",")
    y = line.split(": ")
    z = y[1].split(" ")
    for word in z:
        if word.isdigit() == True:
            x = int(word)
        else:
            if (word == "blue," and x > 14) or (word == "green," and x > 13) or (word == "red," and x > 12):
                valid = False
    if valid == True:
        y = y[0].split(" ")
        total += int(y[1])
print(total)

file = open("day 2/input 2.txt","r")
total = 0
for line in file:
    valid = True
    z = 0
    line = line.strip()
    line = line.replace(";",",")
    x = line.split(": ")
    y = x[1].split(" ")
    for word in y:
        if word.isdigit() == True:
            if int(word) > 14:
                z = 1
            elif int(word) > 13:
                z = 2
            elif int(word) > 12:
                z = 3
            else:
                z = 0
        else:
            if z == 1:
                if word == "blue," or "green," or "red," or "blue" or "green" or "red":
                    valid = False
                    break

            if z == 2:
                if word == "green," or "red," or "green" or "red":
                    valid = False
                    break
            if z == 3:
                if word == "red," or "red":
                    valid = False
                    break
    if valid == True:
        x = x[0].split(" ")
        total += int(x[1])
print(total)
