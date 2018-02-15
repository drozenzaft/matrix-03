from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()
ident(matrix)

print '\n4x4 identity matrix, using ident:\n' + print_matrix(matrix)
#creating translation/multiplication matrix
matrix[0][3] = 60
matrix[1][3] = 60
print 'i will be multiplying the following matrix by the edge matrix:'
print print_matrix(matrix)

points = new_matrix(4,0)
#print '\nempty 4x0 starting matrix:\n' + print_matrix(points)
'''add_edge(points,10,10,0,40,10,0)
add_edge(points,10,10,0,25,40,0)
add_edge(points,40,10,0,25,40,0)'''

add_edge(points,10,10,0,40,10,0)
add_edge(points,10,10,0,10,40,0)
add_edge(points,10,40,0,40,40,0)
add_edge(points,40,10,0,40,40,0)
print 'generating the edge matrix, using 4 add_edge calls\n' + print_matrix(points)

matrix_mult(matrix,points)
print 'after calling matrix_mult(that first matrix, the edge matrix)\n' + print_matrix(points)

matrix_mult(matrix,points)
print 'after calling matrix_mult on the first matrix and the new edge matrix:\n' + print_matrix(points)

a = [[1,2,3],[4,5,6],[7,8,9]]
print 'here is another example. let m1 =\n' + print_matrix(a)
b = [[1,2],[3,4],[5,6]]
print 'let m2 =\n' + print_matrix(b)
matrix_mult(a,b)
print 'this is m2 after matrix_mult(m1,m2):\n' + print_matrix(b)

#now, for the actual image creation part of this

draw_lines( points, screen, color )
display(screen)
