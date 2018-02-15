from display import *
from matrix import *
from drawline import *

def draw_lines( matrix, screen, color ):
    i = 0
    while i < len(matrix[0]):
        draw_line(matrix[0][i],matrix[1][i],matrix[0][i+1],matrix[1][i+1],screen,color)
        i += 2

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix,x0,y0,z0)
    add_point(matrix,x1,y1,z1)

def add_point( matrix, x, y, z=0 ):
    matrix[0].append(x)
    matrix[1].append(y)
    matrix[2].append(z)
    matrix[3].append(1)
