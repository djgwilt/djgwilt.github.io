def solve(calc):
    for i in calc:
        if i == "(":
            index = calc.index(i)
            calc2 = []
            while True:
                if calc[index + 1] == ")":
                    calc.pop(index+1)
                    break
                calc2.append(calc[index + 1])
                calc.pop(index + 1)
            calc[index] = solve(calc2)
    for i in calc:
        if i == "^":
            index = calc.index(i)
            answer = float(calc[index-1]) ** float(calc[index+1])
            calc.pop(index+1)
            calc[index]=answer
            calc.pop(index-1)
        if i == "!":
            index = calc.index(i)
            num = int(calc[index-1])
            answer = num
            for c in range(num-1,1,-1):
                answer *= c
            calc[index] = answer
            calc.pop(index-1)
    for i in calc:
        if i == "*":
            index = calc.index(i)
            answer = float(calc[index-1]) * float(calc[index+1])
            calc.pop(index+1)
            calc[index]=answer
            calc.pop(index-1)
        if i == "/":
            index = calc.index(i)
            answer = float(calc[index-1]) / float(calc[index+1])
            calc.pop(index+1)
            calc[index]=answer
            calc.pop(index-1)
    for i in calc:
        if i == "+":
            index = calc.index(i)
            answer = float(calc[index-1]) + float(calc[index+1])
            calc.pop(index+1)
            calc[index]=answer
            calc.pop(index-1)
        if i == "-":
            index = calc.index(i)
            answer = float(calc[index-1]) - float(calc[index+1])
            calc.pop(index+1)
            calc[index]=answer
            calc.pop(index-1)
    return calc[0]


calc = input()
while calc != "":

    calclist = []
    digit = ""

    for i in calc:
        if i.isdigit() or i == ".":
            digit += i    
        elif digit != "":
            calclist.append(digit)
            digit = ""
            calclist.append(i)
        else:
            calclist.append(i)

    if digit != "":
        calclist.append(digit)

    while len(calclist) > 1:
        ans = solve(calclist)

    if int(ans) == ans:
        ans = int(ans)
    print(ans)
    calc = input()