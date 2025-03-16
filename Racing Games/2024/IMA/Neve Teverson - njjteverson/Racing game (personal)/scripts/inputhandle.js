//function ReduceSpeed (num) {
  //if (num <= 5 && num > 0) num = num - 1 
  //if (num >= -5 && num < 0) num = num + 1
//}


addEventListener("keydown", function(e) {
  if (e.code == 'KeyD') vxr = 5;
  if (e.code == 'KeyA') vxl = -5;
  //if (e.cofde == 'KeyS') vyd = 5;
  //if (e.code == 'KeyW') vyu = -5;
})


addEventListener("keyup", function(e) {
  if (e.code == 'KeyD') vxr = 0;
  if (e.code == 'KeyA') vxl = 0;
  //if (e.code == 'KeyS') vyd = 0;
  //if (e.code == 'KeyW') vyu = 0;
})
