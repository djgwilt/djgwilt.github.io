file = open("day 1/input 1.txt" , "r")
total = 0
for line in file:
    line = line.strip()
    line = line.replace("one","one1one")
    line = line.replace("two","two2two")
    line = line.replace("three","three3three")
    line = line.replace("four","four4four")
    line = line.replace("five","five5five")
    line = line.replace("six","six6six")
    line = line.replace("seven","seven7seven")
    line = line.replace("eight","eight8eight")
    line = line.replace("nine","nine9nine")
    for charachter in line:
        if charachter.isdigit() == True:
            total += int(charachter) * 10
            break
    for charachter in line:
        if charachter.isdigit() == True:
            lastdigit = int(charachter)
    total += lastdigit
    
print(total)


