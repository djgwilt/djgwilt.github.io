// listen for keypress (to detect arrow keys)
document.onkeydown = checkKey

// to store movement direction
let current_level = 0
const levels = [5,9,13,17,21,25,29,33,37,45,63,99,137]
const level_sizes = [100,70,55,40,30,20,15,13,12,10,8,4,3]
let coin_length = 0;
let width = levels[current_level]
let height = width
let settings = {
    Coins: false,
    TimedMovement: false,
}





let game_end = false

const Modes = {
    Hard: 0,
    Ultra: 1,
    Impossible: 2,
    Nightmare: 3,
}
let mode = Modes.Hard;

const Direction = {
    Up: 0,
    Down: 1,
    Left: 2,
    Right: 3,
}


const GoalMode = {
    Random: 0,
    Last:   1,
}
const Goal = GoalMode.Last 
let goalpos = {
    x: 0,
    y: 0
}
const VectorDirection = {
    Up: [0,-1],
    Down: [0,1],
    Left: [-1,0],
    Right: [1,0]
}

let matrix = []

let velocity = {
    x: 0,
    y: 0,
}

// to store current column position
let column = 1
let row    = 1

// to store the handle code for the timer interval to cancel it when we crash
let intervalHandle
if (1){
    let r = document.querySelector(':root');
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
    if (!settings.TimedMovement){
        updatePosition()
        velocity.x = 0
        velocity.y = 0
    }
    
    
}



// the timer check function - runs every 300 milliseconds to update the car position
function updatePosition() {
    
    if (game_end === true) {
       return
    }
    if (settings.TimedMovement){
        
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
		} else if (document.getElementById("r"+row+" c" + column).className === "wall") {
            handleCrash()
        } else if (document.getElementById("r"+row+" c" + column).className === "Goal") { 
            handleWin()
        } else if (document.getElementById("r"+row+" c" + column).className === "Coin") {
            matrix[column][row] = false;
            coin_length--;
            console.log(coin_length)
            document.getElementById("r"+row+" c" + column).className = "God"
            setGoalOnCollectCoin()
        }
        else {
			document.getElementById("r"+row+" c" + column).className = "God"
		}
	}
}

// if the car has gone off the table, this tidies up including crash message
function handleCrash() {
	velocity.x = 0
    velocity.y = 0
	document.getElementById("Message").innerText = "u are bad at game :("
    game_end = true
    current_level = -1
    endGame();
}
function handleWin() {
	velocity.x = 0
    velocity.y = 0
	document.getElementById("Message").innerText = "u win :)"
    game_end = true
    endGame();
}
function generateTable(table) {
  for (let i = 0; i < height; i++) {
    let l = []
    let row = table.insertRow();
    for (let j = 0; j < width; j++) {
        let cell = row.insertCell();
        cell.id = "r"+i+" c"+j
        cell.className = "wall"
     
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

async function setwallSquares(g) {
    for (let r = 0; r < g.length; r++) {
        for (let c = 0; c < g[r].length; c++) {
            let x = "r"+r +" c"+c
         if (g[r][c] === true) {
             document.getElementById(x).className = "wall"
          }
         if (g[r][c] === false) {
             document.getElementById(x).className = "Empty"
         }
         if (g[r][c] === 2) {
             document.getElementById(x).className = "FakeGoal"
             goalpos.x = r
             goalpos.y = c
         } 
         if (g[r][c] === 3) {
             document.getElementById(x).className = "Coin"
         }
         
        }
        
    }
}
function clearwallSquares(){
    for (let r = 0; r < matrix.length; r++) {
        for (let c = 0; c < matrix[r].length; c++) {
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
function getCoinLength() {
  let len = 0;
  for (let r = 0; r < matrix.length; r++) {
        for (let c = 0; c < matrix[r].length; c++) {
             if (matrix[c][r] === 3){
                len++;
             }
        }
  }
  return len
}

class MazeGenerator {
    constructor(width,height) {
        this.width = width
        this.height = height
        this.cells = []
        let temp = []
        for (let i = 0; i < this.width; i++) {
            temp.push(true)
        }
        for (let j = 0; j < this.height; j++) {
            this.cells.push([...temp])
        }
    }
    setPath(x,y) {
        this.cells[y][x] = false
    }
    setwall(x,y) {
        this.cells[y][x] = true 
    }
    iswall(x,y){
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
        let all_directions = shuffleArray([VectorDirection.Up,VectorDirection.Down,VectorDirection.Left,VectorDirection.Right])
       
        while(all_directions.length > 0){

            let current_dir = all_directions.pop()
            let node_x = x + (current_dir[0] * 2)      
            let node_y = y + (current_dir[1] * 2)
            console.log("NODE "+node_x +" "+node_y)
            if (this.iswall(node_x,node_y)) {
                let link_cell_x = x + current_dir[0]
                let link_cell_y = y + current_dir[1]
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
        let s = ""
        const conv = {
            true: "||",
            false: "  "
        }
        for (let y = 0; y < this.height; y++){
            for (let x = 0; x < this.width; x++) {
                s += conv[this.cells[y][x]]
            }
            s += "\n"
        }
        return s
    }
}
function isDeadEnd(tile_x,tile_y) {
    let all_directions = [VectorDirection.Up,VectorDirection.Down,VectorDirection.Left,VectorDirection.Right]
    let number_of_ends = 0
    for (let i = 0; i < all_directions.length; i++) {
        if (getCell(tile_x+all_directions[i][0],tile_y+all_directions[i][1]) == true) {
            number_of_ends++
        }
    }
    return number_of_ends === 3

}


function placeGoal(){
    let possible_goals = []
    for (let r = matrix.length - 1; r >= 0; r--) {
        console.log(r)
        for (let c = matrix[r].length - 1; c >= 0; c--) {
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
    if (!settings.Coins) {return}
    possible_goals.splice(0,1);
    for (let i = 0; i < possible_goals.length; i++) {
        matrix[possible_goals[i][1]][possible_goals[i][0]] = 3
    }
}
function setGoalOnCollectCoin(){
    if (coin_length !== 0) {return}
    else {
      document.getElementById("r"+goalpos.x+" c" + goalpos.y).className = "Goal"

    }
}
function endGame(){
    let r = document.querySelector(':root');
    r.style.setProperty('--size', level_sizes[current_level+1]+"px");
    let t = document.querySelector("#RacingTrack");
    t.innerHTML = ""
    current_level++
    column = 1
    row = 1
    if (current_level != levels.length){
        startGame(current_level)
    } else {
        switch (mode){
            case Modes.Hard:
                
        }
    }
}
async function startGame(level_num){
    width = levels[level_num]
    height = width
    let m = new MazeGenerator(levels[level_num],levels[level_num])
    m.createMaze(Math.round(levels[level_num]/2),Math.round(levels[level_num]/2))
    let t = document.querySelector("#RacingTrack");
    t.innerHTML = ""
    generateTable(t);
    matrix = m.getCells();
    placeGoal();
    console.log(m.getCells())
    await setwallSquares(m.getCells());
    game_end = false
    document.getElementById("r1 c1").className = "God"
    coin_length = getCoinLength()
    if (!settings.Coins) {setGoalOnCollectCoin()}
    
}
function enableHard(){
    settings.Coins = false
    settings.TimedMovement = false
    disableSelection()
    startGame(current_level);
}
function enableUltra(){
    settings.Coins = true
    settings.TimedMovement = false
    disableSelection()
    startGame(current_level);
}
function enableImpossible(){
    settings.Coins = false
    settings.TimedMovement = true
    intervalHandle = setInterval(updatePosition,300)
    disableSelection()
    startGame(current_level);
}
function enableNightmare(){
    settings.Coins = true
    settings.TimedMovement = true
    intervalHandle = setInterval(updatePosition,300)
    disableSelection()
    startGame(current_level);
}


function disableSelection(){
    document.getElementById("buttons").remove()
    document.getElementById("title").innerText = "have fun :D"
}














//startGame(current_level);
