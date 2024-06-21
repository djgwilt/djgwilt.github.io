#############################
# Library Imports
#############################
from js import document, window

#############################
# Global Variables
#############################
audioDrank = document.getElementById("drankdrank")
audioSorryBoutDat = document.getElementById("sorryboutdat")
audioUhHuh = document.getElementById("uh-huh")
audioDKane = document.getElementById("duwapaudio")
audioJace = document.getElementById("hitherwrizz")
audioIntro = document.getElementById("intro")
is_audio_playing = False
# to store current position (x,y)
position = [0, 0]

# to store movement directions (x,y)
direction = [0, 0]

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

#############################
# Sub-Programs
#############################
rappers = ["nettspend", "jace", "yeat", "kankan", "duwap"]
rapperdict = {
    "nettspend": audioDrank,
    "yeat": audioSorryBoutDat,
    "kankan": audioUhHuh,
    "duwap": audioDKane,
    "jace": audioJace,
}
# the function called when a key is pressed - sets direction variable
def checkKey(event):
    event.preventDefault()
    global is_audio_playing
    if not is_audio_playing:
        if event.key == "ArrowRight":
            direction[0] = 1
            direction[1] = 0
        elif event.key == "ArrowLeft":
            direction[0] = -1
            direction[1] = 0
        elif event.key == "ArrowDown":
            direction[1] = 1
            direction[0] = 0
        elif event.key == "ArrowUp":
            direction[1] = -1
            direction[0] = 0
    else:
        direction[0] = 0
        direction[1] = 0


def getCell():
    return document.getElementById("R{}C{}".format(position[1], position[0]))

def checkRappers():
    cell = getCell()
    for rapper in rappers:
        if cell.className == rapper:
            rapperdict[rapper].play()

           
# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition():

    if direction[0] != 0:
        # Set the cell where the car was to empty
        cell = getCell()
        cell.className = ""
        
        # Update the column position for the car
        position[0] += direction[0]

                # Re-draw the car (or report a crash)
        cell = getCell()
        if cell.className in rappers:
            checkRappers()
        if cell == None:
            handleCrash()
        else:
            cell.className = "car"

    elif direction[1] != 0:
        cell = getCell()
        cell.className = ""
        
        # Update the column position for the car
        position[1] += direction[1]

        # Re-draw the car (or report a crash)
        cell = getCell()
        if cell.className in rappers:
            checkRappers()
        if cell == None:
            handleCrash() 
        else:
            cell.className = "car"
    else:
        audioIntro.play()

    
# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you crashed..."

def set_is_audio_playing(is_playing):
    global is_audio_playing
    is_audio_playing = is_playing

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, 300)
    audioIntro.play()
    audioIntro.addEventListener('ended', lambda _: set_is_audio_playing(False))
    


#############################
# Main Program
#############################
audioDrank.autoplay = False
audioDrank.load()
audioIntro.autoplay = False
audioIntro.load()
audioDKane.autoplay = False
audioDKane.load()
audioJace.autoplay = False
audioJace.load()
audioUhHuh.autoplay = False
audioUhHuh.load()
audioSorryBoutDat.autoplay = False
audioSorryBoutDat.load()
runGame()

