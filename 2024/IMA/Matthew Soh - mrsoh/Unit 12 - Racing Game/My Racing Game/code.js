document.onkeydown = checkKey;

let reactorNo = 0;
let width = 11;
let height = 11;

let game_end = false;

// const GoalMode = {
//     Random: 0,
//     Last: 1,
// };
// const Goal = GoalMode.Last;

// let goalpos = {
//     x: 0,
//     y: 0
// };
const directions = [
    [0, -1],
    [0, 1],
    [-1, 0],
    [1, 0]
];

let matrix = [];

let velocity = {
    x: 0,
    y: 0,
};

let column = 1;
let row = 1;
let intervalHandle;
let r = document.querySelector(':root');
r.style.setProperty('--size', "12px");

function shuffleArray(array) {
    let curId = array.length;
    while (curId !== 0) {
        let randId = Math.floor(Math.random() * curId);
        curId -= 1;
        let tmp = array[curId];
        array[curId] = array[randId];
        array[randId] = tmp;
    }
    return array;
}

function checkKey(e) {
    e = e || window.event;
    if (e.keyCode === 39 || e.keyCode === 68) {
        // right arrow
        e.preventDefault();
        velocity.x = 1;
        velocity.y = 0;
    } else if (e.keyCode === 37 || e.keyCode === 65) {
        // left arrow
        e.preventDefault();
        velocity.x = -1;
        velocity.y = 0;
    } else if (e.keyCode === 38 || e.keyCode === 87) {
        // up
        e.preventDefault();
        velocity.x = 0;
        velocity.y = -1;
    } else if (e.keyCode === 40 || e.keyCode === 83) {
        // down
        e.preventDefault();
        velocity.x = 0;
        velocity.y = 1;
    }
    updatePosition();
    velocity.x = 0;
    velocity.y = 0;
}

function updatePosition() {
    if (game_end === true) {
        return;
    }
    if (velocity.x !== 0 || velocity.y !== 0) {
        document.getElementById("R" + row + "C" + column).className = "";
        column += velocity.x;
        row += velocity.y;
        if (!document.getElementById("R" + row + "C" + column)) {
            handleCrash();
        } else if (document.getElementById("R" + row + "C" + column).className === "wall") {
            handleCrash();
        } else if (document.getElementById("R" + row + "C" + column).className === "z") {
            handleWin();
        // } else if (document.getElementById("R" + row + "C" + column).className === "Coin") {
        //     matrix[row][column] = false;
        //     reactorNo--;
        //     document.getElementById("R" + row + "C" + column).className = "kenobi";
        //     // setGoalOnCollectCoin();
        } else {
            document.getElementById("R" + row + "C" + column).className = "kenobi";
        }
    }
}

function handleCrash() {
    velocity.x = 0;
    velocity.y = 0;
    document.getElementById("Message").innerText = "You died.";
    game_end = true;
    current_level = -1;
    endGame();
}

function handleWin() {
    velocity.x = 0;
    velocity.y = 0;
    document.getElementById("Message").innerText = "You win!";
    game_end = true;
    endGame();
}

function generateTable(table) {
    for (let i = 0; i < height; i++) {
        let l = [];
        let row = table.insertRow();
        for (let j = 0; j < width; j++) {
            let cell = row.insertCell();
            cell.id = "R" + i + "C" + j;
            cell.className = "wall";
            l.push(true);
        }
        matrix.push(l);
    }
}

async function setWallSquares(g) {
    for (let r = 0; r < g.length; r++) {
        for (let c = 0; c < g[r].length; c++) {
            let x = "R" + r + "C" + c;
            if (g[r][c]) {
                document.getElementById(x).className = "wall";
            }else{
                document.getElementById(x).className = "";
            }
            // // if (g[r][c] === false) {
            // //     document.getElementById(x).className = "";
            // }
            // if (g[r][c] === 3) {
            //     document.getElementById(x).className = "Coin";
            // }
        }
    }
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// function getCoinLength() {
//     let len = 0;
//     for (let r = 0; r < matrix.length; r++) {
//         for (let c = 0; c < matrix[r].length; c++) {
//             if (matrix[r][c] === 3) {
//                 len++;
//             }
//         }
//     }
//     return len;
// }

class MazeGenerator {
    constructor(width, height) {
        this.width = width;
        this.height = height;
        this.cells = Array.from({ length: this.height }, () => Array(this.width).fill(true));
    }
    createMaze(x, y) {
        console.log(x,y)
        this.cells[y][x] = false;
        let all_directions = shuffleArray(directions);
        // console.log(all_directions)
        for (let dir of all_directions) {
            let node_x = x + (dir[0] * 2);
            let node_y = y + (dir[1] * 2);
        
            if (node_x >= 0 && node_x < this.width && node_y >= 0 && node_y < this.height) {
                console.log(x,y,node_x,node_y, this.cells[y][x], this.cells[node_y][node_x])
                if (this.cells[node_y][node_x]){
                    console.log("linking")
                    let link_cell_x = x + dir[0];
                    let link_cell_y = y + dir[1];
                    this.cells[link_cell_y][link_cell_x] = false;
                    this.createMaze(node_x, node_y);
                }else{
                    console.log("not linking")
                }
                
                // console.log(this.cells)
                
            // }else if (node_x >= 0 && node_x < this.width && node_y >= 0 && node_y < this.height) {
            //     // console.log(x,y,node_x,node_y, this.cells[y][x], this.cells[node_y][node_x])
            //     // console.log(this.cells)
            // }else{
            //     console.log("else",x,y,node_x,node_y)
            //     // console.log(x,y,node_x,node_y, this.cells[y][x], this.cells[node_y][node_x])
            }
        }
    }
    
}

function isDeadEnd(tile_x, tile_y) {
    let number_of_ends = 0;
    for (let i = 0; i < directions.length; i++) {
        if (matrix[tile_y + directions[i][1]] && matrix[tile_y + directions[i][1]][tile_x + directions[i][0]] === true) {
            number_of_ends++;
        }
    }
    return number_of_ends === 3;
}

// function placeGoal() {
//     let possible_goals = [];
//     for (let r = matrix.length - 1; r >= 0; r--) {
//         for (let c = matrix[r].length - 1; c >= 0; c--) {
//             if (matrix[r][c] === false) {
//                 if (c === 1 && r === 1) {
//                     continue;
//                 }
//                 if (isDeadEnd(c, r)) {
//                     possible_goals.push([r, c]);
//                 }
//             }
//         }
//     }
//     if (possible_goals.length === 0) {
//         return;
//     }
//     if (Goal === GoalMode.Random) {
//         possible_goals.sort(() => Math.random() - 0.5);
//     }
//     let goal = possible_goals[0];
//     matrix[goal[0]][goal[1]] = 2;
//     goalpos.x = goal[0];
//     goalpos.y = goal[1];
//     possible_goals.splice(0, 1);
//     for (let i = 0; i < possible_goals.length; i++) {
//         matrix[possible_goals[i][0]][possible_goals[i][1]] = 3;
//     }
// }

// function setGoalOnCollectCoin() {
//     if (reactorNo !== 0) {
//         return;
//     } else {
//         document.getElementById("R" + goalpos.x + "C" + goalpos.y).className = "Goal";
//     }
// }

function endGame() {
    let r = document.querySelector(':root');
    r.style.setProperty('--size', "12px");
    let t = document.querySelector("#RacingTrack");
    t.innerHTML = "";
    current_level++;
    column = 1;
    row = 1;
    startGame(current_level);
}

async function startGame() {
    let m = new MazeGenerator(width, height);
    m.createMaze(Math.floor(width / 2), Math.floor(height / 2));
    let t = document.querySelector("#RacingTrack");
    t.innerHTML = "";
    generateTable(t);
    matrix = m.cells;
    // placeGoal();
    await setWallSquares(m.cells);
    game_end = false;
    document.getElementById("R1C1").className = "kenobi";
    // reactorNo = getCoinLength();
    console.log(m.cells)
}

startGame();
