// listen for keypress (to detect arrow keys)
document.onkeydown = checkKey

// to store movement direction
const levels = [5,9,13,17,25,37,63,99,137]
const level_sizes = [100,75,50,40,30,23,10,6,4]
var width = levels[current_level]
var height = width
var current_level = 0
var game_end = false
const Direction = {
    Up: 0,
    Down: 1,
    Left: 2,
    Right: 3,
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

const GoalMode = {
    Random: 0,
    Last:   1,
}
const Goal = GoalMode.Last 

const VectorDirection = {
    Up: [0,-1],
    Down: [0,1],
    Left: [-1,0],
    Right: [1,0]
}

var matrix = []

var velocity = {
    x: 0,
    y: 0,
}

// to store current column position
var column = 1
var row    = 1

// to store the handle code for the timer interval to cancel it when we crash
var intervalHandle
if (1){
    var r = document.querySelector(':root');
    r.style.setProperty('--size', level_sizes[current_level]+"px");
}
function shuffleArray(array) {
  //return array
  let curId = array.length;
  // There remain elements to shuffle
  while (0 !== curId) {
    // Pick a remaining element
    let randId = Math.floor(Math.random() * curId);
    curId -= 1;
    // Swap it with the current element.
    let tmp = array[curId];
    array[curId] = array[randId];
    array[randId] = tmp;
  }
  return array;
}

// the function called when a key is pressed - sets direction variable
function checkKey(e) {
    // this next line is a workaround for older versions of IE which didn't pass the event as a parameter
    e = e || window.event
    
    if (e.keyCode === 39 || e.keyCode === 68) {
        // right arrow
        e.preventDefault();
	    velocity.x = 1
        velocity.y = 0
    } else if (e.keyCode === 37 || e.keyCode == 65) {
        // left arrow
        e.preventDefault();
	    velocity.x = -1
        velocity.y = 0
    } else if (e.keyCode === 38 || e.keyCode === 87) {
        // up
        e.preventDefault();
        velocity.x = 0
        velocity.y = -1
    } else if (e.keyCode === 40 || e.keyCode === 83) {
        // down
        e.preventDefault();
        velocity.x = 0
        velocity.y = 1
    }
    updatePosition()
    velocity.x = 0
    velocity.y = 0
    
}

// called when the page is loaded to start the timer checks
function runGame() {
	
}

// the timer check function - runs every 300 milliseconds to update the car position
function updatePosition() {
    if (game_end === true) {
       return
    }
	if (velocity.x != 0 || velocity.y != 0) {
        // Set the cell where the car was to empty
		document.getElementById("r"+row+" c" + column).className = "Empty"
        // Update the column position for the car
		column += velocity.x
        row    += velocity.y
        // Re-draw the car (or report a crash)
		if (!document.getElementById("r"+row+" c" + column) ) {
			handleCrash()
		} else if (document.getElementById("r"+row+" c" + column).className === "Wall") {
            handleCrash()
        } else if (document.getElementById("r"+row+" c" + column).className === "Goal") { 
            handleWin()
        }
        else {
			document.getElementById("r"+row+" c" + column).className = "blob"
		}
	}
}

// if the car has gone off the table, this tidies up including crash message
function handleCrash() {
    document.getElementById("r"+row+" c" + column).className = "slime";
    sleep(300).then(() => {
	window.clearInterval(intervalHandle)
	document.getElementById("Message").innerText = "You died"
    game_end = true
    current_level = -1
    endGame();
    });
}
function handleWin() {
	window.clearInterval(intervalHandle)
	document.getElementById("Message").innerText = "Win"
    game_end = true
    endGame();
}
function generateTable(table) {
  for (var i = 0; i < height; i++) {
    var l = []
    let row = table.insertRow();
    for (var j = 0; j < width; j++) {
        let cell = row.insertCell();
        cell.id = "r"+i+" c"+j
        cell.className = "Wall"
     
    }
      matrix.push(l)
  }
    //console.log(matrix)
}
function randomSquare() {
    return Math.floor(Math.random()*(width-1) + 1)
}
function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

async function setWallSquares(g) {
    for (var r = 0; r < g.length; r++) {
        for (var c = 0; c < g[r].length; c++) {
         if (g[r][c] === true) {
             //console.log("yes")
             var x = "r"+r +" c"+c
             document.getElementById(x).className = "Wall"
          }
         if (g[r][c] === false) {
             //console.log("yes")
             var x = "r"+r +" c"+c
             document.getElementById(x).className = "Empty"
             //if (current_level < 6 ){await sleep(10)}
         }
            if (g[r][c] === 2) {
             //console.log("yes")
             var x = "r"+r +" c"+c
             document.getElementById(x).className = "Goal"
         }
         
        }
        
    }
}
function clearWallSquares(){
    for (var r = 0; r < matrix.length; r++) {
        for (var c = 0; c < matrix[r].length; c++) {
         if (matrix[c][r] == 0){
             if (Math.random() < 0.5) {
                // matrix[c][r] = 1
             }
         }
        }
    }
}

function getCell(x,y) {
    try {
    return matrix[y][x]
    } catch {
        return true
    }
}
function setCell(x,y,val) {
    try {
    matrix[y][x] = val
    } catch {
        console.log("NO CELL FOUND " + x + " "+ y)
    }
}
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

class MazeGenerator {
    constructor(width,height) {
        this.width = width
        this.height = height
        this.cells = []
        var temp = []
        for (var i = 0; i < this.width; i++) {
            temp.push(true)
        }
        for (var j = 0; j < this.height; j++) {
            this.cells.push([...temp])
        }
    }
    setPath(x,y) {
        this.cells[y][x] = false
    }
    setWall(x,y) {
        this.cells[y][x] = true 
    }
    isWall(x,y){
        try{
        //console.log(x + " " + y)
        if (x >= 0 && x < this.width && y >= 0 && y < this.width){
            return this.cells[y][x]
        } else {
            return false
        }
        } catch {
            return false
        }
        
      
            
    }
    createMaze(x,y){
        this.setPath(x,y)
        var all_directions = shuffleArray([VectorDirection.Up,VectorDirection.Down,VectorDirection.Left,VectorDirection.Right])
       
        while(all_directions.length > 0){

            var current_dir = all_directions.pop()
            var node_x = x + (current_dir[0] * 2)      
            var node_y = y + (current_dir[1] * 2)
            console.log("NODE "+node_x +" "+node_y)
            if (this.isWall(node_x,node_y)) {
                var link_cell_x = x + current_dir[0]
                var link_cell_y = y + current_dir[1]
                this.setPath(link_cell_x,link_cell_y)
                this.createMaze(node_x,node_y)
            }
        }
        return
    }
    getCells() {
        return this.cells
    }
    printCells() {
        var s = ""
        const conv = {
            true: "||",
            false: "  "
        }
        for (var y = 0; y < this.height; y++){
            for (var x = 0; x < this.width; x++) {
                s += conv[this.cells[y][x]]
            }
            s += "\n"
        }
        return s
    }
}
function isDeadEnd(tile_x,tile_y) {
    var all_directions = [VectorDirection.Up,VectorDirection.Down,VectorDirection.Left,VectorDirection.Right]
    var number_of_ends = 0
    for (let i = 0; i < all_directions.length; i++) {
        if (getCell(tile_x+all_directions[i][0],tile_y+all_directions[i][1]) == true) {
            number_of_ends++
        }
    }
    return number_of_ends === 3

}


function placeGoal(){
    var possible_goals = []
    for (var r = matrix.length - 1; r >= 0; r--) {
        console.log(r)
        for (var c = matrix[r].length - 1; c >= 0; c--) {
         if (matrix[c][r] == 0){
             if (c == 1 && r == 1) {
                 continue
             }
             if (isDeadEnd(r,c)) {
                 possible_goals.push([r,c])
             }
         }
        }
    }
    if (possible_goals.length == 0) {
        return
    }
    if (Goal === GoalMode.Random){
        possible_goals.sort(()=> Math.random()-0.5)
        console.log(possible_goals[0])
        matrix[possible_goals[0][1]][possible_goals[0][0]] = 2
    } else if (Goal === GoalMode.Last){
        matrix[possible_goals[0][1]][possible_goals[0][0]] = 2
    }
}

function endGame(){
    var r = document.querySelector(':root');
    r.style.setProperty('--size', level_sizes[current_level+1]+"px");
    var t = document.querySelector("#RacingTrack");
    t.innerHTML = ""
    current_level++
    column = 1
    row = 1
    if (current_level != levels.length){
        startGame(current_level)
    } else {
        t.innerHTML = "<h1>you have completed the game!! <br> i could add more levels but ur computer would die sorry :D</h1>"
    }
}
async function startGame(level_num){
    width = levels[level_num]
    height = width
    var m = new MazeGenerator(levels[level_num],levels[level_num])
    m.createMaze(Math.round(levels[level_num]/2),Math.round(levels[level_num]/2))
    //m.createMaze(1,1)
    var t = document.querySelector("#RacingTrack");
    t.innerHTML = ""
    generateTable(t);
    matrix = m.getCells();
    placeGoal();
    console.log(m.getCells())
    await setWallSquares(m.getCells());
    game_end = false
    document.getElementById("r1 c1").className = "blob"
}
startGame(current_level);
