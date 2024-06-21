file = open("day 4/input 4.txt","r")
total = 0
for line in file:

    line = line.replace("  "," ")

    line = line.strip()
    line = line.split(": ")
    numbers = line[1].split("| ")
    winning = numbers[0].split(" ")
    numbers = numbers[1].split(" ")

    score = 0

    for x in winning:
        for y in numbers:
            if x == y :
                if score == 0:
                    score += 1
                else:
                    score = score*2
    total += score
print(total)
    


