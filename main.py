from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]


# vertical
draw_line(50, 50, 50, 450, screen, color)
draw_line(450, 450, 450, 50, screen, color)


draw_line(50, 50, 200, 350, screen, color)
draw_line(450, 450, 300, 150, screen, color)
draw_line(50, 100, 400, 450, screen, color)
draw_line(450, 400, 100, 50, screen, color)
draw_line(50, 50, 350, 200, screen, color)
draw_line(450, 450, 150, 300, screen, color)

# horizontal
draw_line(50, 50, 450, 50, screen, color)
draw_line(450, 450, 50, 450, screen, color)

draw_line(50, 450, 350, 300, screen, color)
draw_line(450, 50, 150, 200, screen, color)
draw_line(100, 450, 450, 100, screen, color)
draw_line(400, 50, 50, 400, screen, color)
draw_line(50, 450, 200, 150, screen, color)
draw_line(450, 50, 300, 350, screen, color)

display(screen)
save_extension(screen, 'img.png')
