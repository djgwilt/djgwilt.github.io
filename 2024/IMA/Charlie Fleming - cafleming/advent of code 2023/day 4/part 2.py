file = open("day 4/input 4.txt","r")
count = 0
total = 0
c2 = 1
tovisit = []
while c2 <=188:
    tovisit.append(c2)
    c2 +=1
yournum = []
winnum = []

for line in file:

    line = line.replace("  "," ")
    line = line.strip()
    line = line.split(": ")
    numbers = line[1].split(" | ")
    winnum.append(numbers[0].split(" "))
    yournum.append(numbers[1].split(" "))
print(winnum[0])
print(yournum[0])


for x in tovisit:
        score = 0
        for y in yournum[x-1]:
            for z in winnum[x-1]:
                if y == z:
                    score += 1
        c = 1
        while score > 0:
            if x+c <= 187:
                tovisit.append(x+c)
            c += 1
            score = score - 1
        total += 1
        tovisit.pop(0)

print(total)