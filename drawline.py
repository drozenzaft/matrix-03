from display import *

#octave 1
def draw_line1( x0, y0, x1, y1, screen, color ):
    x = x0
    y = y0
    A = y1 - y0
    B = x0 -x1
    d = 2*A + B
    while x <= x1:
        plot(screen,color,x,y)
        if d > 0:
            y += 1
            d += 2*B
        x += 1
        d += 2*A

#octave 2
def draw_line2( x0, y0, x1, y1, screen, color):
    x = x0
    y = y0
    A = y1 - y0
    B = x0 - x1
    d = A + 2*B
    while y <= y1:
        plot(screen, color, x, y)
        if d < 0:
            x += 1
            d += 2*A
        y += 1
        d += 2*B

#octave 7
def draw_line7( x0, y0, x1, y1, screen, color):
    x = x0
    y = y0
    A = y1 - y0
    B = x0 - x1
    d = A - 2*B
    while y >= y1:
        plot(screen, color, x, y)
        if d > 0:
            x += 1
            d += 2*A
        y -= 1
        d -= 2*B

#octave 8
def draw_line8( x0, y0, x1, y1, screen, color ):
    x = x0
    y = y0
    A = y1 - y0
    B = x0 -x1
    d = 2*A - B
    while x <= x1:
        plot(screen,color,x,y)
        if d < 0:
            y -= 1
            d -= 2*B
        x += 1
        d += 2*A

#all octaves
def draw_line( x0, y0, x1, y1, screen, color):
    if (x0 == x1):
        if y0 < y1:
            draw_line2(x0,y0,x1,y1,screen,color)
        else:
            draw_line7(x0,y0,x1,y1,screen,color)
        return
    if (x1 < x0):
        a = x1
        x1 = x0
        x0 = a
        a = y1
        y1 = y0
        y0 = a
    m = ((y1-y0)*1.0)/(x1-x0)
    if (m >= 0):
        if (m <= 1):
            draw_line1(x0,y0,x1,y1,screen,color)
        else:
            draw_line2(x0,y0,x1,y1,screen,color)
    else:
        if (m >= -1):
            draw_line8(x0,y0,x1,y1,screen,color)
        else:
            draw_line7(x0,y0,x1,y1,screen,color)
