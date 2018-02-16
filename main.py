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
print "enjoy the checkerboard image, it's also on the gallery\n(albeit without a border for the white corners, but please excuse that)!\n"

#checkerboard creator
def fill(x,y,side):
    matrix = new_matrix(4,0)
    i = 0
    while y+i <= side:
        add_edge(matrix,x,y+i,0,x+side,y+i,0)
        i += 1
    return matrix
def checkerboard():
    matrix = new_matrix(4,0)
    for r in range(10):
        for c in range(10):
            i = 0
            if (c+r)%2 == 1:
                while i <= 50:
                    add_edge(matrix,c*50,r*50+i,0,c*50+50,r*50+i,0)
                    i += 1
    draw_lines(matrix, screen, [255,255,255])
    #adding border
    matrix = new_matrix(4,0)
    add_edge(matrix,0,0,0,0,500,0)
    add_edge(matrix,0,0,0,500,0,0)
    add_edge(matrix,0,500,0,500,500,0)
    add_edge(matrix,500,0,0,500,500,0)
    draw_lines(matrix, screen, [0,0,0])

checkerboard()

display(screen)
