from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()
ident(matrix)
for i in range(3):
    matrix[i][3] = 60
print print_matrix(matrix)

points = new_matrix(4,0)
add_edge(points,10,10,0,40,10,0)
add_edge(points,10,10,0,25,40,0)
add_edge(points,40,10,0,25,40,0)
print print_matrix(points)

matrix_mult(matrix,points)
print print_matrix(points)

draw_lines( points, screen, color )
display(screen)
