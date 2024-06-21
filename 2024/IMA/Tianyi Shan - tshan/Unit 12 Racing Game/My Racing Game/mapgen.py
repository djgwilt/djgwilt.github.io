def generategrid():
    global grid
    for a in range(HEIGHT):
        row = []
        for b in range(WIDTH):
            row.append("O")
        grid.append(row)

def rungrid():
    global grid
    runposition = [1,1]
    gen = True
    while gen == True:
        determinelist = []
        grid[runposition[0]][runposition[1]] = ""
        gonorth = True
        gosouth = True
        goeast = True
        gowest = True
        if runposition[0] == 1 and runposition[1] == 1:
            gonorth = False
            gowest = False
        if runposition[0] == WIDTH - 2 and runposition[1] == HEIGHT - 2:
            gosouth = False
            goeast = False
        if runposition[0] == 1:
            gowest = False
        if runposition[1] == 1:
            gonorth = False
        if runposition[0] == WIDTH - 2:
            goeast = False
        if runposition[1] == HEIGHT - 2:
            gosouth = False
        determinelist.append(gonorth)
        determinelist.append(gosouth)
        determinelist.append(goeast)
        determinelist.append(gowest)
        print(determinelist)
        gen = False      
        
WIDTH = 10
HEIGHT = 10
grid = []
generategrid()
rungrid()
