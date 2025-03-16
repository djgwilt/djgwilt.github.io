#############################
# Library Imports
#############################

from js import document,window

#############################
# Global Variables
#############################

# to store current position (x,y)
position1 = [0, 0]
position2 = [0, 0]
soupposition = [8, 0]

# to store movement directions (x,y)
direction1 = [0, 0]
direction2 = [0, 0]
player = "player_1"
IsSoupHeld = False
# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

# Audio
audioGhlghl = document.getElementById("audioGhlghl")
audioWhatIsLove = document.getElementById("audioWhatIsLove")

#############################
# Sub-Programs
#############################

# the function called when a key is pressed - sets direction variable
while True:
    audioWhatIsLove.autoplay = True
    audioWhatIsLove.load()
    def checkKey(event):
        global player
        event.preventDefault()
        print(event.key)
        if event.key == "ArrowRight":
            direction1[0] = 1
            direction1[1] = 0
        elif event.key == "ArrowLeft":
            # left arrow
            direction1[0] = -1
            direction1[1] = 0
        elif event.key == "ArrowUp":
            direction1[0] = 0
            direction1[1] = -1
        elif event.key == "ArrowDown":
            direction1[0] = 0
            direction1[1] = 1
        elif event.key == " ":
            if player == "player_1":
                player = "player_2"
            else:
                player = "player_1"
                audioGhlghl.play()
        #elif event.key == "f":
            IsSoupHeld=True


    def getCell(position):
        return document.getElementById("R{}C{}".format(position[1], position[0]))

    # the timer check function - runs every 300 milliseconds to update the car position
    def updatePosition():
        global position1

        if direction1[0] != 0 or direction1[1] != 0:
            # Set the cell where the car was to empty


            oldpos = list(position1)

            # Update the column position for the car
            position1[0] += direction1[0]
            position1[1] += direction1[1]

            # Re-draw the car (or report a crash)
            cell1 = getCell(position1)

            if cell1 == None:
                #handleCrash()
                position1 = oldpos
            elif cell1.className == "weakwall":
                if player == "player_2":
                    oldcell = getCell(oldpos)
                    oldcell.className = ""
                    cell1.className = player
                else:
                    position1 = oldpos
            else:
                oldcell = getCell(oldpos)
                oldcell.className = ""
                cell1.className = player

            #     if direction1[0] != 0:
            # #Character 2
            # cell2 = getCell()
            # cell2.className = ""

            # # Update the column position for the car
            # position[0] += direction[0]

            # # Re-draw the car (or report a crash)
            # cell2 = getCell()
            # if cell2 == None:
            #     handleCrash()
            # else:
            #     cell2.className = "player_2"

    # if the car has gone off the table, this tidies up including crash message
    def handleCrash():
        window.clearInterval(intervalHandle)
        document.getElementById("Message").innerText = "Oops you crashed..."

    # called when the page is loaded to start the timer checks
    def runGame():
        global intervalHandle
        print("Running Game")
        document.addEventListener('keydown', checkKey)
        intervalHandle = window.setInterval(updatePosition, 300)

    #############################
    # Main Program
    #############################

    audioGhlghl.autoplay = False
    audioGhlghl.load()
    runGame()