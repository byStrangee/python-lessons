const ctx = c.getContext('2d');

c.width = innerWidth;
c.height = innerHeight;

c.style.background = ['#151515']

function hexColor() {
      return "#" + (
            Math.round(
                  Math.random() * 0xffffff
            )
            .toString(16)
      )
}
class Circle {
      constructor(x, y, c, dx, dy){
            this.x = x
            this.y = y
            this.radius = c
            this.dx = dx;
            this.dy = dy
      }
      draw() {
            ctx.beginPath();
            ctx.strokeStyle = hexColor()
            ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
            ctx.stroke();
            // ctx.fill()
      }
      move() {
            if(this.x > innerWidth - this.radius || this.x < 0) {
                  this.dx = -this.dx
            }
            if(this.y > innerHeight - this.radius || this.y  < 0) {
                  this.dy = -this.dy
            }
            this.x += this.dx
            this.y += this.dy
      }
}
circles = []
for (let i = 0; i < 350; i++ ) 
{
      let x = Math.random() * innerWidth
      let y = Math.random() * innerHeight
      let rad = Math.random() * 50 + 10
      let dx = Math.random() + Math.random()
      let dy = Math.random() + Math.random()
      circles.push(
            new Circle(x, y, rad, dx, dy)
      )
}


function move() {
      requestAnimationFrame(move)
      ctx.clearRect(0, 0, innerWidth, innerHeight) // comment it if u want
      circles.forEach(
            circle => {
                  circle.draw()
                  circle.move()
            }
      )
}
move()