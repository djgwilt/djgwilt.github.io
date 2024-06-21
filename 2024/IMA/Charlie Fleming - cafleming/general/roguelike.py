import random

def attack(enemyhealth,health,enemy):
    enemyhit = random.randint(1,100)
    playerhit = random.randint(1,100)
    if enemyhit <= 50:
        health -= 1
        print("the {} hit".format(enemy[3]))
    if playerhit <= hitchance:
        enemyhealth -= 1
        print("you hit")
    return health, enemyhealth

def PrintGrid(grid , health, coins):
    for i in grid:
        line = ""
        for i2 in i:
            line += i2
        print(line)
    print(f"health: {health}, coins: {coins}, WASD to move, SPACE to interact")

def doors(level,enemys,grid):
    if level == 1:
        if enemys[0] == "dead":
            grid[5][11] = "."
        if enemys[1] == "dead" and enemys[2] == "dead":
            grid[11][17] = "."
        if enemys[3] == enemys[4] == enemys[5] == "dead":
            grid[7][62] = "."
        if enemys[6] =="dead":
            grid[3][62] = "."
            grid[8][57] = "."
        if enemys[7] == "dead":
            grid[15][64] = "."
    elif level == 2:
        alldead = True
        for enemy in enemys:
            if enemy != "dead":
                alldead == False
        if alldead:
            grid[18][70] = "."
    elif level == 3:
        if enemys[0] == "dead":
            grid[3][1] = "."
            grid[3][68] = "/"
            grid[15][60] = "."
            print("")
    return grid

def PrintShop(shop):
    print()
    return



level = 1
health = 30
coins = 1
hitchance = 50
def levelreset(level):
    grid = []
    levelname = "map"+str(level)+".txt"
    file = open(levelname,"r")
    for line in file:
        line= line.strip()#
        grid.append([])
        for i in line:
            grid[-1].append(i)
    file.close()
    
    charPos = [1,1]
    grid[charPos[0]][charPos[1]] = "#"

    if level == 1:
        enemys = [[2,4,28,"goblin","G",2],[2,11,4,"goblin","G",2],[2,11,7,"goblin","G",2],[2,4,47,"goblin","G",2],[3,5,52,"orc","O",4],[2,7,58,"goblin","G",2],[3,8,74,"orc","O",4],[5,13,53,"Troll","T",6]]
        people = [[3,3,"the troll is hiding deep in the forest, you'll have to ight your way to him, you can use the coins you get from defeated enemys at the %."],[17,73,"you defeated the troll, well done.(step on the ! to proceed)"]]
        shops = [[3,8]]
    elif level == 2:
        enemys = [[1,7,15,"Zombie","Z",1],[1,9,10,"Zombie","Z",1],[1,12,12,"Zombie","Z",1],[1,8,32,"Zombie","Z",1],[1,9,43,"Zombie","Z",1],[1,14,28,"Zombie","Z",1],[1,18,23,"Zombie","Z",1],[1,9,60,"Zombie","Z",1]]
        people = [[3,3,"the deamon lives in the catacombs under the church, just over there"]]
        shops = []
    elif level == 3:
        enemys = [[10,10,44,"Deamon","D",12]] 
        people = []
        shops = []

    for enemy in enemys:
        grid[enemy[1]][enemy[2]] = enemy[4]
    if people != []:
        for person in people:
            grid[person[0]][person[1]] = "@"

    if level == 1:
        print("chapter 1: the adventure begins")
        print("something about a troll")
        print("(press enter to proceed)")
        input()
    if level == 2:
        print("chapter 2: the catacombs")
        print("you're first adventure was a great sucess, something about a deamon")
        input()
    if level == 5:
        print("chapter 3: the mountain")
        input()

    PrintGrid(grid,health,coins)
    return grid, charPos, enemys, people, shops


grid, charPos, enemys, people, shops = levelreset(level)
movement = input()
while movement != "end":
    if movement == "w":
        if grid[charPos[0]-1][charPos[1]] == ".":
            grid[charPos[0]][charPos[1]] = "."
            charPos[0] -= 1
            grid[charPos[0]][charPos[1]] = "#"
        elif grid[charPos[0]-1][charPos[1]] == "!":
            level += 1
            grid,charPos, enemys, people, shops = levelreset(level)

    if movement == "d":
        if grid[charPos[0]][charPos[1]+1] == ".":
            grid[charPos[0]][charPos[1]] = "."
            charPos[1] += 1
            grid[charPos[0]][charPos[1]] = "#"
        elif grid[charPos[0]][charPos[1]+1] == "!":
            level += 1
            grid, charPos, enemys, people, shops = levelreset(level)

    if movement == "s":
        if grid[charPos[0]+1][charPos[1]] == ".":
            grid[charPos[0]][charPos[1]] = "."
            charPos[0] += 1
            grid[charPos[0]][charPos[1]] = "#"
        elif grid[charPos[0]+1][charPos[1]] == "!":
            level += 1
            grid,charPos, enemys, people, shops = levelreset(level)

    if movement == "a":
        if grid[charPos[0]][charPos[1]-1] == ".":
            grid[charPos[0]][charPos[1]] = "."
            charPos[1] -= 1
            grid[charPos[0]][charPos[1]] = "#"
        elif grid[charPos[0]][charPos[1]-1] == "!":
            level += 1
            grid, charPos, enemys, people, shops = levelreset(level)

    if movement == " ":
        for enemy in enemys:
            if enemy[1] in range(charPos[0]-1,charPos[0]+2) and enemy[2] in range(charPos[1]-1,charPos[1]+2):
                print(f"it's an evil {enemy[3]}")
                index = enemys.index(enemy)
                health , enemy[0] = attack(enemys[index][0],health,enemy)
        for person in people:
            if person[0] in range(charPos[0]-1,charPos[0]+2) and person[1] in range(charPos[1]-1,charPos[1]+2):
                print(person[2])
        for shop in shops:
            if shop[0] in range(charPos[0]-1,charPos[0]+2) and shop[1] in range(charPos[1]-1,charPos[1]+2):
               PrintShop(shop) 

    if movement == "F":
        break

    if health == 0:
        print("game over")
        break

    for enemy in enemys:
        if enemy[0] == 0:
            coins += enemy[5]
            print("enemy defeated")
            grid[enemy[1]][enemy[2]] = "."
            index = enemys.index(enemy)
            enemys[index] = "dead"
            grid = doors(level,enemys,grid)

    PrintGrid(grid,health,coins)
    


    movement = input()


