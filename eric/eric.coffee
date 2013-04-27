dx = 20
[nx, ny] = [30, 20]
canvas = document.getElementById 'canvas'

canvas.width = nx*dx
canvas.height = ny*dx

state = []
for i in [1..ny] by 1
  line = []
  line.push 0 for j in [1..nx] by 1
  state.push line

ctx = canvas.getContext '2d'

color = [
  'rgb(255, 255, 255)',
  'rgb(204, 255, 255)',
  'rgb(153, 255, 255)',
  'rgb(102, 255, 255)',
  'rgb(51, 255, 255)',
  'rgb(0, 255, 255)',
]

redraw = () =>
  for i in [0..ny-1] by 1
    for j in [0..nx-1] by 1
      ctx.fillStyle = color[state[i][j]]
      ctx.fillRect j*dx, i*dx, dx, dx

canvas.onmousemove = (e) =>
  if (e.pageX || e.pageY)
    [x, y] = [e.pageX, e.pageY]
  else
    x = e.clientX + document.body.scrollLeft + document.documentElement.scrollLeft
    y = e.clientY + document.body.scrollTop + document.documentElement.scrollTop
  x -= canvas.offsetLeft
  y -= canvas.offsetTop
  [i, j] = [Math.floor(y/dx), Math.floor(x/dx)]
  state[i][j] += 1
  state[i][j] %= 6
  redraw()

