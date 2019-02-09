from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

draw_line(50, 50, 450, 450, screen, color)
draw_line(50, 50, 450, 50, screen, color)
draw_line(50, 50, 350, 200, screen, color)

display(screen)
save_extension(screen, 'img.png')
