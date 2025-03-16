const settings = {
  difficultyLevels: {
    easy: 1000,
    medium: 2000,
    hard: 3000,
  },
  boardWidth: 1200,
  boardHeight: 1200,
  initialSnakeLength: 5,
};

let currentDifficulty = 'easy'; // Default difficulty level
let game; // To store the setInterval reference

const canvas = document.createElement('canvas');
const context = canvas.getContext('2d');
canvas.width = settings.boardWidth;
canvas.height = settings.boardHeight;
document.body.appendChild(canvas);

let snake = [];
for (let i = settings.initialSnakeLength - 1; i >= 0; i--) {
  snake.push({ x: i, y: 0 });
}

let direction = 'RIGHT';
let food = {
  x: Math.floor(Math.random() * (settings.boardWidth / 10)),
  y: Math.floor(Math.random() * (settings.boardHeight / 10)),
};

// EvilBird object
const evilBird = {
  x: Math.floor(Math.random() * (settings.boardWidth / 10)), // Random initial x
  y: Math.floor(Math.random() * (settings.boardHeight / 10)), // Random initial y
  image: new Image(), // Create an image object for the EvilBird
};
evilBird.image.src = 'EvilBird.jpg'; // Set the image source

document.addEventListener('keydown', changeDirection);

function changeDirection(event) {
  if (event.key === 'a' && direction !== 'RIGHT') direction = 'LEFT';
  else if (event.key === 'w' && direction !== 'DOWN') direction = 'UP';
  else if (event.key === 'd' && direction !== 'LEFT') direction = 'RIGHT';
  else if (event.key === 's' && direction !== 'UP') direction = 'DOWN';
}

function update() {
  const head = { x: snake[0].x, y: snake[0].y };

  if (direction === 'LEFT') head.x--;
  else if (direction === 'UP') head.y--;
  else if (direction === 'RIGHT') head.x++;
  else if (direction === 'DOWN') head.y++;

  snake.unshift(head);

  // EvilBird Movement (towards the snake's head)
  const headX = snake[0].x;
  const headY = snake[0].y;
  if (headX > evilBird.x) evilBird.x += 0.1; // Move right
  else if (headX < evilBird.x) evilBird.x -= 0.1; // Move left
  if (headY > evilBird.y) evilBird.y += 0.1; // Move down
  else if (headY < evilBird.y) evilBird.y -= 0.1; // Move up

  // EvilBird-Snake Collision Detection
  if (headX === Math.round(evilBird.x) && headY === Math.round(evilBird.y)) {
    clearInterval(game);
    alert('You died - the Evil Bird got you!');
  }

  if (head.x === food.x && head.y === food.y) {
    food = {
      x: Math.floor(Math.random() * (settings.boardWidth / 10)),
      y: Math.floor(Math.random() * (settings.boardHeight / 10)),
    };
  } else {
    snake.pop();
  }

  if (head.x < 0 || head.x >= settings.boardWidth / 10 || head.y < 0 || head.y >= settings.boardHeight / 10 || collision(head)) {
    clearInterval(game);
    alert('You died');
  }
}

function collision(head) {
  for (let i = 4; i < snake.length; i++) {
    if (head.x === snake[i].x && head.y === snake[i].y) return true;
  }
  return false;
}

function draw() {
  context.fillStyle = 'black';
  context.fillRect(0, 0, canvas.width, canvas.height);

  context.fillStyle = 'white';
  snake.forEach((part) => context.fillRect(part.x * 10, part.y * 10, 10, 10));

  context.fillStyle = 'red';
  context.fillRect(food.x * 10, food.y * 10, 10, 10);

  // Draw the EvilBird
  context.drawImage(evilBird.image, evilBird.x * 10, evilBird.y * 10, 100, 100); 
}

function gameLoop() {
  update();
  draw();
}

function setDifficulty(difficulty) {
  currentDifficulty = difficulty;
  clearInterval(game);
  game = setInterval(gameLoop, 1000 / settings.difficultyLevels[currentDifficulty]);
}

// Start the game at the default difficulty
game = setInterval(gameLoop, 1000 / settings.difficultyLevels[currentDifficulty]);