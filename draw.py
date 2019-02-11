from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    x = x0
    y = y0
    A = y1 - y0
    B = -(x1 - x0)
    if B <= 0:
        if A >= 0:
            if A <= -B:
                d = 2 * A + B
                while x <= x1:
                    plot(screen, color, x, y)
                    if d >= 0:
                        y += 1
                        d += 2 * B
                    x += 1
                    d += 2 * A
            else:
                d = A + 2 * B
                while y <= y1:
                    plot(screen, color, x, y)
                    if d <= 0:
                        x += 1
                        d += 2 * A
                    y += 1
                    d += 2 * B
        else:
            if A >= B:
                d = 2 * A + -B
                while x <= x1:
                    plot(screen, color, x, y)
                    if d <= 0:
                        y -= 1
                        d -= 2 * B
                    x += 1
                    d += 2 * A
            else:
                d = A + -2 * B
                while y >= y1:
                    plot(screen, color, x, y)
                    if d >= 0:
                        x += 1
                        d += 2 * A
                    y -= 1
                    d -= 2 * B
    else:
        draw_line(x1, y1, x0, y0, screen, color)
                    
