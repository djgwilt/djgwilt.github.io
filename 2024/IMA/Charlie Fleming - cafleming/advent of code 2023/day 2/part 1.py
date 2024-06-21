valid = True
gameindex = ""
gameindexx = 0
results = ""
total = 0

file = open("day 2/input 2.txt","r")

for line in file:
    line = line.strip()
    line = line.split(": ")

    valid = True

    if gameindexx == 100:
        break
    gameindex = line[0]
    gameindex = gameindex.split(" ")
    gameindexx = int(gameindex[1])

    results = line[1]
    results = results.replace(";",",")
    results = results.split(", ")
    for result in results:
        result = result.split(" ")
        if int(result[0]) > 12 and result[1] == "red":
            valid = False
        elif int(result[0]) > 13 and result[1] == "green":
            valid = False
        elif int(result[0]) > 14 and result[1] == "blue":
            valid = False
    
    if valid == True:
        total += gameindexx

print(total)