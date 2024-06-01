$(document).ready(function(){
  init();
});

var canvas;  
var ctx;
var x = 0;
var y = 0;
var dx = 2;
var dy = 4;
var width = 0;
var height = 0; 

function circle(x,y,r) {
  ctx.beginPath();
  ctx.arc(x, y, r, 0, Math.PI*2, true);
  ctx.fill();
}

function rect(x,y,w,h) {
  ctx.beginPath();
  ctx.rect(x,y,w,h);
  ctx.closePath();
  ctx.fill();
}

 
function reset() {
  ctx.clearRect(0, 0, width, height);
}

function init() {
  canvas = document.getElementById("canvas");
  width = canvas.width;
  height = canvas.height;
  ctx = canvas.getContext("2d");
  return setInterval(animate, 10);
}


function animate() {
  reset();
  ctx.fillStyle = "#FAF7F8";
  rect(0,0,width,height);
  ctx.fillStyle = "#444444";
  circle(x, y, 10);

  if (x + dx > width || x + dx < 0)
    dx = -dx;
  if (y + dy > height || y + dy < 0)
    dy = -dy;

  x += dx;
  y += dy;
}