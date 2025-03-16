//THE BASICS
const canvas = document.getElementById("canvas"); //creates canvas
const ctx = canvas.getContext("2d"); //sets type to 2d
const CANVAS_HEIGHT = canvas.height = 550
const CANVAS_WIDTH = canvas.width = 550
const Background = document.getElementById("Background")

//VARIABLES

let score = 0;
let count = 0;
let speed = 3;
let maxSpeed = 15;

//centre
let x = 250; //starts at x pos 250
let y = 350; //starts at y pos 250
let ex = 255; //starts pothole at x pos 255
let ey = 0; //starts pothole at y pos 0 (top of the screen)
ex = Math.floor(Math.random()*500)

//movement
let vxr = 0;
let vxl = 0;
let vyu = 0;
let vyd = 0;

//player
let pwidth = 50;
let pheight = 50;

//enemy
let ewidth = 40;
let eheight = 40;

//check whether movement allowed
let ableToMoveL = true;
let ableToMoveR = true;
//let ableToMoveU = true;
//let ableToMoveD = true;

//booleans
var GameOver = false
var UpdateScore = true
var ProduceEnemies = true

//refreshes screen
function update(){
  ctx.clearRect(0, 0, canvas.width, canvas.height)
  ctx.drawImage(Background, 0, 0)

  //reset movement allowed since it won't automatically go back
  ableToMoveL = true;
  ableToMoveR = true;
  //ableToMoveU = true;
  //ableToMoveD = true;

  //allowed to move?
  if (x > 495) ableToMoveR = false;
  if (x < 5) ableToMoveL = false;
  //if (y > 495) ableToMoveD = false;
  //if (y < 5) ableToMoveU = false;

  //ReduceSpeed(vxr)
  //ReduceSpeed(vxl)

  //excecutes if allowed
  if (ableToMoveR == true) x += vxr;
  if (ableToMoveL == true) x += vxl;
  //if (ableToMoveU == true) y += vyu;
  //if (ableToMoveD == true) y += vyd;

  //makes pothole (enemy)
  //while (ProduceEnemies == true) {
  ctx.fillStyle = "#000000";
  ctx.fillRect(ex, ey, ewidth, eheight);
  //}

  //changes how fast the enemy comes back depending on how fast the car is supposed to be going
  ey = ey + speed
  if (ey > 550)
    ey = -100;
  if (ey == -100) ex = Math.floor(Math.random()*500);

  //makes player
  ctx.fillStyle = "#000000"
  ctx.fillRect(x, y, pwidth, pheight)
  ctx.drawImage(player, 0, 0, 385, 647, x-20, y-20, 90, 120) //displaces it since photo not cropped correctly

  //collision detection: enemies
  if ((x + 25 > ex && x + 25 < ex + 50) && (y + 25 < ey + 50 && y + 25 > ey)) {
    GameOver = true;
    //console.log('true');
  }

  //death screen
  if (GameOver == true) {
    ctx.fillStyle = "#000000"
    ctx.fillRect(100, 225, 350, 100)
    ctx.fillStyle = "#FFFFFF"
    ctx.font="60px sans-serif";
    ctx.fillText('GAME OVER', 125, 295, 300)
    UpdateScore = false;
    ProduceEnemies = false;
  }

  //score counter
  ctx.fillStyle = "black";
  ctx.fillRect(5,5,100,45)
  ctx.fillStyle = "#fcba03";
  ctx.font="35px sans-serif";
  ctx.fillText(score + 'xp', 10, 40, 90) 

  //speedometer
  ctx.fillStyle = "#3F88C5";
  ctx.beginPath();
  ctx.arc(500, 500, 40, 0, 2 * Math.PI);
  ctx.fill();
  ctx.lineWidth = 3
  ctx.strokeStyle = "#1C3144";
  ctx.stroke();

  //speedometer reading
  //ctx.fillStyle = "black";
  //ctx.fillRect(475,475,50,50)
  ctx.fillStyle = "#D00000";
  ctx.font="35px sans-serif";
  ctx.fillText(speed + 'mps', 470, 510, 60)

  if (count % 30 == 0 && UpdateScore == true) score = score + 1
  if (count % 100 == 0 && speed < maxSpeed && UpdateScore == true) speed = speed + 1
  count = count + 1

  requestAnimationFrame(update)
  
}


//PROGRAM
update()