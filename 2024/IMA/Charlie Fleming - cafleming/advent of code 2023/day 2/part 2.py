file = open("day 2\input 2.txt","r")
total = 0
for line in file:

    blue = 0
    green = 0
    red = 0

    line = line.strip()
    line = line.split(": ")
    line = line[1].replace(";" , ",")
    line = line.split(", ")

    for part in line:

        part = part.split(" ")

        if (part[1] == "blue") and (int(part[0]) > blue):
            blue = int(part[0])
        elif (part[1] == "green") and (int(part[0]) > green):
            green = int(part[0])
        elif (part[1] == "red") and (int(part[0]) > red):
            red = int(part[0])
    
    total += blue*green*red

print(total)