window.onload = function()
{
	x = 0;
	y = 0;
	speed = 5;
	angle = 0;
	mod = 0;
	
	canvas = document.getElementById("canvas");
	context = canvas.getContext("2d");
	car = new Image();
    car.src="data:image/jpg;base64,/9j/4AAQSkZJRgABAQEAlgCWAAD/2wBDAAMCAgMCAgMDAwMEAwMEBQgFBQQEBQoHBwYIDAoMDAsKCwsNDhIQDQ4RDgsLEBYQERMUFRUVDA8XGBYUGBIUFRT/2wBDAQMEBAUEBQkFBQkUDQsNFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBT/wAARCAE3ATcDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD9U6KKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAoooo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NHIAc7WGzkHvXvFr8CfhzY3cF1beBvD8FzBIssU0emxKyOpyrAheCCAQfau6orqp0o0r8h8/jcxxOYOLxDT5drRjH/0lITpwOlfOX7U37DvgX9pq1bULiL+wPGMabINes1w7AdEmXpIufXkc7SMnP0dRWp5p+KHxI/YV+NnwcuJFPh7/AITDRIyduoaM4cqgxgsjEFc56fN0rydvD+tRSeXPoWrW0uSPLnsJkPHB6rzzX9A9VLvSbG/cPc2VvcOOjTRKx/UVXMB+A/8Awi+tcH+xtSx/15yf/E1v+GPgz488ZXyWmjeENYvbhxlV+yPGCPUFwAfzr91P+Ef0vAH9mWeB0/cJ/hV2KGOCMJEixoOiqMAU+YD8z/gf/wAEyfEWvXlvqHxHvk0PSlIc6ZYPvuZh12s+MIM8EAE46Eda/RPwL4D0D4a+GbPw/wCGtMg0nSrRNkcECgfVmPVmJySx5JJJ610FFTe4BXzf4u/Ya8I+MPFWr67PresW0+pXUl3JFCYtiu7FmxlCcZJr6QormrYeliElVjex7OWZzmGTTlUy+q6bkrO1tV8z5Y/4d7+DP+hi1384f/iKP+He/gz/AKGLXfzh/wDiK+p6K5f7Own/AD7R9F/r1xJ/0GS/D/I+V2/4J7eC2Uj/AISLXefeH/43X0n4X8Pw+FfDun6PbySSwWUKwo8mNxA7nFatFdFHC0cO26UbXPFzPiDNM5hGnmFd1FF3V7aP5IKKKK6j54KKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooA//2Q==";

    window.addEventListener("keydown", keypress_handler, false);
    window.addEventListener("keyup", keyup_handler, false);

	var move = setInterval(function()
	{
		draw();
	}, 30);
};

function draw()
{
	context = canvas.getContext("2d");
	context.clearRect(0, 0, 800, 800);

	context.fillStyle = "rgb(200, 100, 220)";
	context.fillRect(500, 500, 100, 100);

	x += (speed*mod) * Math.cos(Math.PI/180 * angle);
	y += (speed*mod) * Math.sin(Math.PI/180 * angle);

	context.save();
	context.translate(x, y);
	context.rotate(Math.PI/180 * angle);
	context.drawImage(car, -(car.width/2), -(car.height/2));	
	context.restore();
}

function keyup_handler(event)
{
	if(event.keyCode == 87 || event.keyCode == 83)
	{
		mod = 0;
	}
}

function keypress_handler(event)
{
	console.log(event.keyCode);
	if(event.keyCode == 87)
	{
		mod = 1;
	}
	if(event.keyCode == 83)
	{
		mod = -1;
	}
	if(event.keyCode == 65)
	{
		angle -= 5;
	}
	if(event.keyCode == 68)
	{
		angle+=5;
	}
}