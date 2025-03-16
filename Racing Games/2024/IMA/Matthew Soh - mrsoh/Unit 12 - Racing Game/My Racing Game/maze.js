const directions = [
    [0, -1],
    [0, 1],
    [-1, 0],
    [1, 0]
];

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
let m = new MazeGenerator(3,3)
m.createMaze(0,0)
console.table(m.cells)