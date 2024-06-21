addEventListener("keydown", function(e) {
  console.log(e)
  if (e.code == 'KeyD') vxr = SPEED;
  if (e.code == 'KeyA') vxl = -SPEED;
  if (e.code == 'KeyW') vyd = -SPEED;
  if (e.code == "KeyS") vyu = SPEED;
})


addEventListener("keyup", function(e) {
  if (e.code == 'KeyD') vxr = ZERO;
  if (e.code == 'KeyA') vxl = ZERO;
  if (e.code == "KeyW") vyd = ZERO;
  if (e.code == "KeyS") vyu = ZERO;
})