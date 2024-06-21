console.log("Successfully loaded Game")
//success

//CONSTANT VARIABLES
const Canvas = document.getElementById("Canvas");
console.log("Successfully loaded Canvas")
const ctx = Canvas.getContext("2d");
console.log("Successfully loaded Context")
const CWIDTH = 500; //CHANGE LATER
const CHEIGHT = 500;
const ORIGIN = 0;
const ZERO = 0;
const SPEED = 5;
const GAMEOVERX = 0;
const GAMEOVERY = 0;
const GAMEOVERWIDTH = 500;
const GAMEOVERHEIGHT = 500;


//BOOLEANS
var UpdateSuccessful = false;
var ableToMoveDown = true;
var ableToMoveUp = true;
var ableToMoveLeft = true;
var ableToMoveRight = true;
var objectiveReached = false;
var eableToMoveDown = true;
var eableToMoveUp = true;
var eableToMoveLeft = true;
var eableToMoveRight = true;

//CLASSES
class WALL {
  constructor(height, width, leftx, topy, colour, objective) {
    //setting the parameters to class objects
    this.height = height;
    this.width = width;
    this.leftx = leftx;
    this.rightx = leftx + width;
    this.topy = topy;
    this.bottomy = topy + height;
    this.colour = colour;
    this.objective = objective;
  }

  //START ENEMY CODE
  enemyMove(ey, ex, x, y) {
    eableToMoveDown = true;
    eableToMoveUp = true;
    eableToMoveLeft = true;
    eableToMoveRight = true;
    if ((ey + ewidth == this.topy)&&(ex + ewidth > this.leftx)&&(ex < this.rightx)) {
      eableToMoveDown = false; 
      console.log('Enemy can\'t go down')
    }
    if ((ey == this.bottomy)&&(ex < this.rightx)&&(ex + ewidth > this.leftx)) {
      eableToMoveUp = false; 
      console.log('Enemy can\'t go up');
    }
    if ((ex == this.rightx)&&(ey < this.bottomy)&&(ey + eheight > this.topy)) {
      eableToMoveLeft = false; 
      console.log('Enemy can\'t go left');
    }
    if ((ex + ewidth == this.leftx)&&(ey < this.bottomy)&&(ey + eheight > this.topy)) {
      eableToMoveRight = false; 
      console.log('Enemy can\'t go right');
    }
    let xDistance = ex - x
    let yDistance = ey - y
    if (xDistance > 0 && eableToMoveLeft == true) {ex = ex - 1; console.log('Move left');} //enemy further right than player
    if (xDistance < 0 && eableToMoveRight == true) {ex = ex + 1; console.log('Move right');} //enemy further left than player
    if (yDistance > 0 && eableToMoveUp == true) {ey = ey - 1; console.log('Move Up')}//enemy further down than player
    if (yDistance < 0 && eableToMoveDown == true) {ey = ey + 1; console.log('Move Down')} //enemy further up than player
    if (xDistance == 0) console.log('Same distance x');
    if (yDistance == 0) console.log('Same distance y');
    console.log('ex co-ordinates are: ' + ex, ey)
  }

  //END ENEMY CODE



  //collision
  collisionCheck(x,y) {
    if ((y + width == this.topy)&&(x + width > this.leftx)&&(x < this.rightx)) {

      ableToMoveDown = false; 
      //console.log('Can\'t go down')
      if (this.objective == true) {
        console.log('Objective reached');
        objectiveReached = true;
      }
    }
    if ((y == this.bottomy)&&(x < this.rightx)&&(x + width > this.leftx)) {

      ableToMoveUp = false; 
      //console.log('Can\'t go up');
      if (this.objective == true) {
        console.log('Objective reached');
        objectiveReached = true;
      }
    }
    if ((x == this.rightx)&&(y < this.bottomy)&&(y + height > this.topy)) {
      
      ableToMoveLeft = false; 
      //console.log('Can\'t go left');
      if (this.objective == true) {
        console.log('Objective reached');
        objectiveReached = true;
      }
    }
    if ((x + width == this.leftx)&&(y < this.bottomy)&&(y + height > this.topy)) {

      ableToMoveRight = false; 
      //console.log('Can\'t go right');
      if (this.objective == true) {
        console.log('Objective reached');
        objectiveReached = true;
      }
    } 
  }
  
  drawWall(){
    ctx.fillStyle = this.colour; //REPLACE COLOUR
    ctx.fillRect(this.leftx, this.topy, this.width, this.height);
  }
}

function randomInt(max, min) {
  number = 0
  while (number <= (min/5)) {
    number = (Math.random() * (max/5));
    if (number <= (min/5)) console.log('Too small');
  }
  return (Math.floor(number))*5;
}

function randomColour() {

}

const wall1 = new WALL(200,20,50,50,"#969696",false);
const wall2 = new WALL(20,200,100,300,"#969696",false);
const wall3 = new WALL(30,30,470,470,"#0A2472", true);
const wall4 = new WALL(randomInt(200,30),20,randomInt(500,0),randomInt(500, 0),"#969696",false)

wallList = [wall1, wall2, wall3, wall4]

//LET VARIABLES
let width = 50;
let height = 50;
let x = CWIDTH/2 - height/2;
let y = CHEIGHT/2 - width/2;
let ground = y
let vxr = ZERO;
let vxl = ZERO;
let vyd = ZERO;
let vyu = ZERO;
let count = ZERO;
let wallLeftx = 50;
let wallWidth = 100;
let wallRightx = wallLeftx + wallWidth;
let wallHeight = 20;
let wallTopy = 50;
let wallBottomy = wallTopy + wallHeight;
let eheight = 50;
let ewidth = 50;
let ex = CWIDTH/2 - ewidth/2;
let ey = CWIDTH - eheight;

//FUNCTIONS
//Out of bounds?
//||((y + width >= wallTopy)&&(y < wallBottomy)&&(x + width > wallLeftx)&&(x < wallRightx))
function outOfBoundsCheck() {
  ableToMoveDown = true;
  ableToMoveUp = true;
  ableToMoveLeft = true;
  ableToMoveRight = true;
  if ((y + width> CWIDTH)) ableToMoveDown = false;
  if (y < 0) ableToMoveUp = false;
  if (x < 0) ableToMoveLeft = false;
  if (x + width > CWIDTH) ableToMoveRight = false;
  for (let i = 0; i < wallList.length; i++) {
    wallList[i].collisionCheck(x,y)
    wallList[i].enemyMove(ey, ex, x, y)
  }
  //console.log(x)
}


y = 0;

//Refresh window
function update(){
  UpdateSuccessful = true;
  outOfBoundsCheck()

  ctx.clearRect(ORIGIN, ORIGIN, CWIDTH, CHEIGHT)
  //console.log(x,y)

  ctx.fillStyle = "Green"; //REPLACE COLOUR
  ctx.fillRect(x, y, width, height);
  ctx.lineWidth =  1;
  ctx.strokeStyle = "White"
  ctx.strokeRect(x, y, width, height);
  if (ableToMoveRight == true) x += vxr;
  if (ableToMoveLeft == true) x += vxl;
  if (ableToMoveUp == true) y += vyd;
  if (ableToMoveDown == true) y += vyu;

  ctx.fillStyle = "Red"; //REPLACE COLOUR
  ctx.fillRect(ex, ey, ewidth, eheight);
  ctx.lineWidth =  1;
  ctx.strokeStyle = "White"
  ctx.strokeRect(ex, ey, ewidth, eheight);
   
  for (let i = 0; i < wallList.length; i++) {
    wallList[i].drawWall()
  }



  if (objectiveReached == true) {
    ctx.fillStyle = "Black";
    console.log('confirmed')
    ctx.fillRect(GAMEOVERX, GAMEOVERY, GAMEOVERWIDTH, GAMEOVERHEIGHT);
    ctx.fillStyle = "White";
    ctx.font = "bold 50px sans-serif";
    ctx.fillText('LEVEL CLEARED', 100,250,300);
  }

  //console.log(randomInt(20, 10))

  requestAnimationFrame(update)
}

update()
if (UpdateSuccessful == true) {
console.log("Successfully loaded Update function")

}

