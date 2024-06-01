#############################
# Library Imports
#############################
from js import document, window
#############################
# Global Variables
#############################

# increase delay to slow down
delay = 300
delay_2 = delay
# set all the variables for car_1
if True:
    # to get where the car is
    try:
        car = document.getElementsByClassName("Car")[0].id
        next_cross = ""
    except:
        car = document.getElementsByClassName("Car_cross")[0].id
        next_cross = document.getElementsByClassName("Car_cross")[0]


    # set next_up etc. to nothing
    next_up, next_down, next_left, next_right = "", "", "", ""
    up, down, left, right = False, False, False, False
    last_pressed = ""

    # set black to False
    black, curr_black = "", False

    column = int(car[3])
    row = int(car[1])
    try:
        Tunnel_1_id = document.getElementsByClassName("Tunnel_1")[0].id
        Tunnel_2_id = document.getElementsByClassName("Tunnel_2")[0].id
        Tunnel_1 = [int(Tunnel_1_id[1]), int(Tunnel_1_id[3])]
        Tunnel_2 = [int(Tunnel_2_id[1]), int(Tunnel_2_id[3])]
    except:
        pass
    xDir = 0
    yDir = 0
    left_right = "right"
    coins = 0
    total_coins = len(document.getElementsByClassName("Coin")) + len(document.getElementsByClassName("Coin_cross"))
    facing = "U"

# set all the variables for car_2
try:
    # to get where the car is
    try:
        car_2 = document.getElementsByClassName("Car_2")[0].id
        next_cross_2 = ""
    except:
        car_2 = document.getElementsByClassName("Car_cross_2")[0].id
        next_cross_2 = document.getElementsByClassName("Car_cross_2")[0]


    # set next_up_2 etc. to nothing
    next_up_2, next_down_2, next_left_2, next_right_2 = "", "", "", ""
    up_2, down_2, left_2, right_2 = False, False, False, False
    last_pressed_2 = ""

    # set black to False
    black_2, curr_black_2 = "", False

    column_2 = int(car_2[3])
    row_2 = int(car_2[1])
    xDir_2 = 0
    yDir_2 = 0
    left_right_2 = "right"
    facing_2 = "U"
except:
    pass


has_crashed = False

doors = []
doors2 = []
keys = 0
pressed = False
pressed_2 = False

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0
intervalHandle2 = 0

#############################
# Sub-Programs
#############################

# the function called when a key is pressed - sets direction variable
def checkKey(event):
    # globals for car_1
    global xDir
    global yDir
    global row
    global column
    global left_right
    global has_crashed
    global speed
    global facing
    global next_up, next_down, next_left, next_right, up, down, left, right, last_pressed
    global pressed
    # globals for car_2
    global xDir_2
    global yDir_2
    global row_2
    global column_2
    global left_right_2
    global has_crashed_2
    global speed_2
    global facing_2
    global next_up_2, next_down_2, next_left_2, next_right_2, up_2, down_2, left_2, right_2, last_pressed_2
    global pressed_2
    
    if has_crashed == False:
        if event.keyCode == 39:
            if right == True or (left == False and up == False and down == False):
                # right arrow
                last_pressed = "r"
                xDir = 1
                yDir = 0
                getCell().className = "Car"
                left_right = "right"
                facing = "R"
                right = False
            else:
                handleCrash()
            pressed = True
        elif event.keyCode == 37:
            if left == True or (right == False and up == False and down == False):
                # left arrow
                last_pressed = "l"
                xDir = -1
                yDir = 0
                getCell().className = "Car_left"
                left_right = "left"
                facing = "L"
                left = False
            else:
                handleCrash()
            pressed = True
        elif event.keyCode == 38 or event.keyCode == 16:
            event.preventDefault()
            if up == True or (left == False and right == False and down == False):
                # up arrow
                last_pressed = "u"
                yDir = -1
                xDir = 0
                facing = "U"
                up = False
            else:
                handleCrash()
            pressed = True
        elif event.keyCode == 40:
            event.preventDefault()
            if down == True or (left == False and up == False and right == False):
                # down arrow
                last_pressed = "d"
                yDir = 1
                xDir = 0
                facing = "D"
                down = False
            else:
                handleCrash()
            pressed = True
        
        
        elif event.keyCode == 68:
            if right_2 == True or (left_2 == False and up_2 == False and down_2 == False):
                # right arrow_2
                last_pressed_2 = "r"
                xDir_2 = 1
                yDir_2 = 0
                getCell_2().className = "Car_2"
                left_right_2 = "right"
                facing_2 = "R"
                right_2 = False
            else:
                handleCrash()
            pressed_2 = True
        elif event.keyCode == 65:
            if left_2 == True or (right_2 == False and up_2 == False and down_2 == False):
                # left arrow_2
                last_pressed_2 = "l"
                xDir_2 = -1
                yDir_2 = 0
                getCell_2().className = "Car_left_2"
                left_right_2 = "left"
                facing_2 = "L"
                left_2 = False
            else:
                handleCrash()
            pressed_2 = True
        
        elif event.keyCode == 87:
            if up_2 == True or (left_2 == False and right_2 == False and down_2 == False):
                # up arrow
                last_pressed_2 = "u"
                yDir_2 = -1
                xDir_2 = 0
                facing_2 = "U"
                up_2 = False
            else:
                handleCrash()
            pressed_2 = True
        elif event.keyCode == 83:
            if down_2 == True or (left_2 == False and up_2 == False and right_2 == False):
                # down arrow
                last_pressed_2 = "d"
                yDir_2 = 1
                xDir_2 = 0
                facing_2 = "D"
                down_2 = False
            else:
                handleCrash()
            pressed_2 = True
        
# functions for car_1
def getCell():
    return document.getElementById(f"R{row}C{column}")

def getCellName():
    return f"R{row}C{column}"

# the timer check function - runs every {delay} milliseconds to update the car position
def updatePosition():
    global column
    global row
    global coins
    global total_coins
    global left_right
    global has_crashed
    global Tunnel_1
    global Tunnel_2
    global keys
    global next_cross
    global next_up, next_down, next_left, next_right, up, down, left, right, last_pressed
    global pressed
    global xDir, yDir
    global facing
    global black, curr_black
    if has_crashed != True:
        
        # if nothing was pressed see if you need to initiate a crash because of the arrows
        if pressed == False:
            if last_pressed == "r":
                if right == True or (left == False and up == False and down == False):
                    # right arrow
                    last_pressed = "r"
                    xDir = 1
                    yDir = 0
                    getCell().className = "Car"
                    left_right = "right"
                    facing = "R"
                    right = False
                else:
                    handleCrash()
            elif last_pressed == "l":
                if left == True or (right == False and up == False and down == False):
                    # left arrow
                    last_pressed = "l"
                    xDir = -1
                    yDir = 0
                    getCell().className = "Car_left"
                    left_right = "left"
                    facing = "L"
                    left = False
                else:
                    handleCrash()
            elif last_pressed == "u":
                if up == True or (left == False and right == False and down == False):
                    # up arrow
                    last_pressed = "u"
                    yDir = -1
                    xDir = 0
                    facing = "U"
                    up = False
                else:
                    handleCrash()
            elif last_pressed == "d":
                if down == True or (left == False and up == False and right == False):
                    # down arrow
                    last_pressed = "d"
                    yDir = 1
                    xDir = 0
                    facing = "D"
                    down = False
                else:
                    handleCrash()
        
        try:
            if xDir != 0 or yDir != 0:
                # Set the cell where the car was to empty
                cell = getCell()
                # check if you need to turn back to a black
                if black != "":
                    black.className = "Black"
                    black = ""
                    curr_black = False
                else:
                    try:
                        if curr_black == False:
                            cell.className = "Empty"
                    except:
                        pass


                # Update the column position for the car
                column += xDir
                # Update the row position for the car
                row += yDir
                # Re-draw the car (or report a crash)
                cell = getCell()
                # if you go through the tunnel 1
                try:
                    if cell.className == "Tunnel_1" and cell.className != "Open_portal":
                        print("Entered a tunnel")
                        if facing == "U":
                            row = Tunnel_2[0]-1
                            column = Tunnel_2[1]
                        elif facing == "D":
                            row = Tunnel_2[0] + 1
                            column = Tunnel_2[1]
                        elif facing == "L":
                            row = Tunnel_2[0]
                            column = Tunnel_2[1] - 1
                        elif facing == "R":
                            row = Tunnel_2[0]
                            column = Tunnel_2[1] + 1
                        cell = getCell()
                    # if you go through the tunnel 2
                    if cell.className == "Tunnel_2" and cell.className != "Open_portal":
                        print("Entered a tunnel")
                        if facing == "U":
                            row = Tunnel_1[0]-1
                            column = Tunnel_1[1]
                        elif facing == "D":
                            row = Tunnel_1[0] + 1
                            column = Tunnel_1[1]
                        elif facing == "L":
                            row = Tunnel_1[0]
                            column = Tunnel_1[1] - 1
                        elif facing == "R":
                            row = Tunnel_1[0]
                            column = Tunnel_1[1] + 1
                        cell = getCell()
                except:
                    pass

                # check if you need to turn a cross into a wall
                if next_cross != "":
                    next_cross.className = "Wall"
                    next_cross = ""

                
                
                # check if you need to turn back to up/down/left/right tile
                if next_up != "":
                    next_up.className = "Up"
                    next_up = ""
                elif next_down != "":
                    next_down.className = "Down"
                    next_down = ""
                elif next_left != "":
                    next_left.className = "Left"
                    next_left = ""
                elif next_right != "":
                    next_right.className = "Right"
                    next_right = ""

                if cell and cell.className != "Wall" and cell.className != "Closed_portal" and cell.className != "Closed_door" and cell.className != "Closed_door_2" and cell.className != "Closed_door_3":
                    if cell.className == "Coin" or cell.className == "Coin_cross":
                        coins += 1
                    if cell.className == "Key":
                        while len(document.getElementsByClassName("Closed_door")) != 0:
                            getDoors()
                        if left_right == "right":
                            cell.className = "Car"
                        elif left_right == "left":
                            cell.className = "Car_left"
                    if cell.className == "Key_2":
                        while len(document.getElementsByClassName("Closed_door_2")) != 0:
                            getDoors2()
                        if left_right == "right":
                            cell.className = "Car"
                        elif left_right == "left":
                            cell.className = "Car_left"
                    if cell.className == "Key_3":
                        keys += 1
                        document.getElementById("keys").innerText = keys
                        if left_right == "right":
                            cell.className = "Car"
                        elif left_right == "left":
                            cell.className = "Car_left"

                    if cell.className == "Cross" or cell.className == "Coin_cross":
                        next_cross = cell
                    # check if the cell being entered is an up/down/left/right tile
                    if cell.className == "Up":
                        next_up = cell
                    elif cell.className == "Down":
                        next_down = cell
                    elif cell.className == "Left":
                        next_left = cell
                    elif cell.className == "Right":
                        next_right = cell
                    
                   
                        
                    # check if you've gotten to the open portal
                    if cell.className == "Open_portal":
                        if left_right == "right":
                            cell.className = "Car_on_portal"
                            has_crashed = True
                            window.clearInterval(intervalHandle)
                            window.clearInterval(intervalHandle2)
                        else:
                            cell.className = "Car_left_on_portal"
                            has_crashed = True
                            window.clearInterval(intervalHandle)
                            window.clearInterval(intervalHandle2)
                        print("You win!!!!")
                        audio = document.getElementById("Win")
                        audio.autoplay = True
                        audio.load()
                        document.getElementById("next_level").className = "show"
                        window.clearInterval(intervalHandle)
                        window.clearInterval(intervalHandle2)
                    # check if the upcoming tile is black
                    elif cell.className == "Black":
                        black = cell
                        cell.className = "Black"
                        curr_black = True




                    else:
                        if coins == total_coins:
                            portals = document.getElementsByClassName("Closed_portal")
                            for i in range(len(portals)):
                                document.getElementsByClassName("Closed_portal")[0].className = "Open_portal"
                        if left_right == "right":
                            try:
                                cell.className = "Car"
                            except:
                                handleCrash()
                        elif left_right == "left":
                            try:
                                cell.className = "Car_left" 
                            except:
                                handleCrash()
                else:
                    try:
                        if cell.className == "Closed_door_3" and keys != 0:
                            keys -= 1
                            if left_right == "right":
                                cell.className = "Open_door_3_right"
                            elif left_right == "left":
                                cell.className = "Open_door_3_left"
                            document.getElementById("keys").innerText = keys
                        else:
                            handleCrash()
                    except:
                        handleCrash()



                # make sure you can only go one way after an arrow tile
                if next_up != "":
                    up = True
                    down = False
                    right = False
                    left = False
                elif next_down != "":
                    up = False
                    down = True
                    right = False
                    left = False
                elif next_left != "":
                    up = False
                    down = False
                    left = True
                    right = False
                elif next_right != "":
                    up = False
                    down = False
                    left = False
                    right = True
        except:
            print("Fail")
        pressed = False

# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    global has_crashed
    window.clearInterval(intervalHandle)
    window.clearInterval(intervalHandle2)
    audio = document.getElementById("Crash")
    audio.autoplay = True
    audio.load()
    if has_crashed == False:
        print("Crashed")
        print("Reload the page to restart (ctrl + r)")
    has_crashed = True
    document.getElementById("Message").innerText = "Oops you crashed..."
    try:
        document.getElementsByClassName("fixed1")[0].style.color = "#8B0000"
        document.getElementsByClassName("fixed1")[0].innerText = "Crashed!!!"
    except:
        document.getElementsByClassName("fixed3")[0].style.color = "#8B0000"
        document.getElementsByClassName("fixed3")[0].innerText = "Crashed!!!"

# open the doors when a key is picked up
def getDoors():
    global doors
    doors = document.getElementsByClassName("Closed_door")
    for i in doors:
        if i.className == "Closed_door":
            i.className = "Open_door"

def getDoors2():
    global doors2
    doors2 = document.getElementsByClassName("Closed_door_2")
    for i in doors2:
        if i.className == "Closed_door_2":
            i.className = "Open_door_2"
            

# functions fot car_2
def getCell_2():
    return document.getElementById(f"R{row_2}C{column_2}")

def getCellName_2():
    return f"R{row_2}C{column_2}"

def updatePosition_2():
    try:
        global column_2
        global row_2
        global coins, total_coins
        global left_right_2
        global has_crashed
        global Tunnel_1
        global Tunnel_2
        global keys
        global next_cross_2
        global next_up_2, next_down_2, next_left_2, next_right_2, up_2, down_2, left_2, right_2, last_pressed_2
        global pressed_2
        global xDir_2, yDir_2
        global facing_2
        global black_2, curr_black_2
        if has_crashed != True:
            cell_2 = getCell_2()
            # if nothing was pressed see if you need to initiate a crash because of the arrows
            if pressed_2 == False:
                if last_pressed_2 == "r":
                    if right_2 == True or (left_2 == False and up_2 == False and down_2 == False):
                        # right arrow_2
                        last_pressed_2 = "r"
                        xDir_2 = 1
                        yDir_2 = 0
                        getCell_2().className = "Car_2"
                        left_right_2 = "right"
                        facing_2 = "R"
                        right_2 = False
                    else:
                        handleCrash()
                elif last_pressed_2 == "l":
                    if left_2 == True or (right_2 == False and up_2 == False and down_2 == False):
                        # left arrow_2
                        last_pressed_2 = "l"
                        xDir_2 = -1
                        yDir_2 = 0
                        getCell_2().className = "Car_left_2"
                        left_right_2 = "left"
                        facing_2 = "L"
                        left_2 = False
                    else:
                        handleCrash()
                elif last_pressed_2 == "u":
                    if up_2 == True or (left_2 == False and right_2 == False and down_2 == False):
                        # up arrow
                        last_pressed_2 = "u"
                        yDir_2 = -1
                        xDir_2 = 0
                        facing_2 = "U"
                        up_2 = False
                    else:
                        handleCrash()
                elif last_pressed_2 == "d":
                    if down_2 == True or (left_2 == False and up_2 == False and right_2 == False):
                        # down arrow
                        last_pressed_2 = "d"
                        yDir_2 = 1
                        xDir_2 = 0
                        facing_2 = "D"
                        down_2 = False
                    else:
                        handleCrash()
            
            pressed_2 = False
            #try:
            if xDir_2 != 0 or yDir_2 != 0:
                # Set the cell where the car was to empty
                cell_2 = getCell_2()
                # check if you need to turn back to a black
                if black_2 != "":
                    black_2.className = "Black"
                    black_2 = ""
                    curr_black_2 = False
                else:
                    try:
                        if curr_black_2 == False:
                            cell_2.className = "Empty"
                    except:
                        pass
                


                # Update the column position for the car
                column_2 += xDir_2
                # Update the row position for the car
                row_2 += yDir_2
                # Re-draw the car (or report a crash)
                cell_2 = getCell_2()
                # if you go through the tunnel 1
                
                try:
                    if cell_2.className == "Tunnel_1" and cell_2.className != "Open_portal":
                        print("Entered a tunnel")
                        if facing_2 == "U":
                            row_2 = Tunnel_2[0]-1
                            column_2 = Tunnel_2[1]
                        elif facing_2 == "D":
                            row_2 = Tunnel_2[0] + 1
                            column_2 = Tunnel_2[1]
                        elif facing_2 == "L":
                            row_2 = Tunnel_2[0]
                            column_2 = Tunnel_2[1] - 1
                        elif facing_2 == "R":
                            row_2 = Tunnel_2[0]
                            column_2 = Tunnel_2[1] + 1
                        cell_2 = getCell_2()
                    # if you go through the tunnel 2
                    if cell_2.className == "Tunnel_2" and cell_2.className != "Open_portal":
                        print("Entered a tunnel")
                        if facing_2 == "U":
                            row_2 = Tunnel_1[0]-1
                            column_2 = Tunnel_1[1]
                        elif facing_2 == "D":
                            row_2 = Tunnel_1[0] + 1
                            column_2 = Tunnel_1[1]
                        elif facing_2 == "L":
                            row_2 = Tunnel_1[0]
                            column_2 = Tunnel_1[1] - 1
                        elif facing_2 == "R":
                            row_2 = Tunnel_1[0]
                            column_2 = Tunnel_1[1] + 1
                        cell_2 = getCell_2()
                except:
                    pass
                
                # check if you need to turn a cross into a wall
                if next_cross_2 != "":
                    next_cross_2.className = "Wall"
                    next_cross_2 = ""
                

                
                # check if you need to turn back to up/down/left/right tile
                if next_up_2 != "":
                    next_up_2.className = "Up"
                    next_up_2 = ""
                elif next_down_2 != "":
                    next_down_2.className = "Down"
                    next_down_2 = ""
                elif next_left_2 != "":
                    next_left_2.className = "Left"
                    next_left_2 = ""
                elif next_right_2 != "":
                    next_right_2.className = "Right"
                    next_right_2 = ""
                if cell_2 and cell_2.className != "Wall" and cell_2.className != "Closed_portal" and cell_2.className != "Closed_door" and cell_2.className != "Closed_door_2" and cell_2.className != "Closed_door_3":
                    # check if coin is getting picked up by car_2
                    if cell_2.className == "Coin" or cell_2.className == "Coin_cross":
                        coins += 1
                    if cell_2.className == "Key":
                        while len(document.getElementsByClassName("Closed_door")) != 0:
                            getDoors()
                        if left_right_2 == "right":
                            cell_2.className = "Car_2"
                        elif left_right_2 == "left":
                            cell_2.className = "Car_left_2"
                    if cell_2.className == "Key_2":
                        while len(document.getElementsByClassName("Closed_door_2")) != 0:
                            getDoors2()
                        if left_right_2 == "right":
                            cell_2.className = "Car"
                        elif left_right_2 == "left":
                            cell_2.className = "Car_left"
                    if cell_2.className == "Key_3":
                        keys += 1
                        document.getElementById("keys").innerText = keys
                        if left_right_2 == "right":
                            cell_2.className = "Car"
                        elif left_right_2 == "left":
                            cell_2.className = "Car_left"

                    if cell_2.className == "Cross" or cell_2.className == "Coin_cross" or cell_2.className == "Coin_cross_2":
                        next_cross_2 = cell_2
                    # check if the cell being entered is an up/down/left/right tile
                    if cell_2.className == "Up":
                        next_up_2 = cell_2
                    elif cell_2.className == "Down":
                        next_down_2 = cell_2
                    elif cell_2.className == "Left":
                        next_left_2 = cell_2
                    elif cell_2.className == "Right":
                        next_right_2 = cell_2



                    # check if you've gotten to the open portal
                    if cell_2.className == "Open_portal":
                        if left_right_2 == "right":
                            cell_2.className = "Car_on_portal_2"
                            has_crashed = True
                            window.clearInterval(intervalHandle)
                            window.clearInterval(intervalHandle2)
                        else:
                            cell_2.className = "Car_left_on_portal_2"
                            has_crashed = True
                            window.clearInterval(intervalHandle)
                            window.clearInterval(intervalHandle2)
                        print("You win!!!!")
                        audio = document.getElementById("Win")
                        audio.autoplay = True
                        audio.load()
                        document.getElementById("next_level").className = "show"
                        window.clearInterval(intervalHandle)
                        window.clearInterval(intervalHandle2)
                    # check if the upcoming tile is black
                    elif cell_2.className == "Black":
                        black_2 = cell_2
                        cell_2.className = "Black"
                        curr_black_2 = True




                    else:
                        if coins == total_coins:
                            portals = document.getElementsByClassName("Closed_portal")
                            for i in range(len(portals)):
                                document.getElementsByClassName("Closed_portal")[0].className = "Open_portal"
                    if left_right_2 == "right":
                        try:
                            cell_2.className = "Car_2"
                        except:
                            handleCrash()
                    elif left_right_2 == "left":
                        try:
                            cell_2.className = "Car_left_2" 
                        except:
                            handleCrash()
                else:
                    try:
                        if cell_2.className == "Closed_door_3" and keys != 0:
                            keys -= 1
                            if left_right_2 == "right":
                                cell_2.className = "Open_door_3_right"
                            elif left_right_2 == "left":
                                cell_2.className = "Open_door_3_left"
                            document.getElementById("keys").innerText = keys
                        else:
                            handleCrash()
                    except:
                        handleCrash()



                # make sure you can only go one way after an arrow tile
                if next_up_2 != "":
                    up_2 = True
                    down_2 = False
                    right_2 = False
                    left_2 = False
                elif next_down_2 != "":
                    up_2 = False
                    down_2 = True
                    right_2 = False
                    left_2 = False
                elif next_left_2 != "":
                    up_2 = False
                    down_2 = False
                    left_2 = True
                    right_2 = False
                elif next_right_2 != "":
                    up_2 = False
                    down_2 = False
                    left_2 = False
                    right_2 = True
            #except:
            #    print("Fail_2")
                
    except:
        pass


#############################
# Main Program
#############################
# called when the page is loaded to start the timer checks

def set_speed(el):
    global delay, delay_2
    global intervalHandle, intervalHandle2
    try:
        delay = int(document.getElementById("delay").value)
        delay_2 = delay
        document.addEventListener('keydown', checkKey)
        window.clearInterval(intervalHandle)
        window.clearInterval(intervalHandle2)
        intervalHandle = window.setInterval(updatePosition, delay)
        intervalHandle2 = window.setInterval(updatePosition_2, delay_2)
        print(f"Speed is at {delay}")
    except:
        pass
    
def runGame():
    global intervalHandle
    global intervalHandle2
    global delay, delay_2
    print("Running Game")
    try:
        document.getElementsByClassName("fixed1")[0].style.color = "#00C000"
        document.getElementsByClassName("fixed1")[0].innerText = "GO!!!"
    except:
        document.getElementsByClassName("fixed3")[0].style.color = "#00C000"
        document.getElementsByClassName("fixed3")[0].innerText = "GO!!!"
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, delay)
    intervalHandle2 = window.setInterval(updatePosition_2, delay_2)

document.getElementById("btn").onclick = set_speed

runGame()
