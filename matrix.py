import math


def print_matrix( matrix ):
    s = ""
    for r in matrix:
        for c in r:
            if c / 10 == 0:
                s += '  ' + str(c) + ' '
            elif c / 10 <= 10:
                s += ' ' + str(c) + ' '
                
            else:
                s += str(c) + ' '
        s += '\n'
    return s
def ident( matrix ):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if r == c:
                matrix[r][c] = 1
            else:
                matrix[r][c] = 0

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    ans = new_matrix(len(m1), len(m2[0]))
    for cellr in range(len(ans)):
        for cellc in range(len(ans[0])):
            for c in range(len(ans)):
               ans[cellr][cellc] += m1[cellr][c] * m2[c][cellc]
    print "ans: \n"+ print_matrix(ans)
  #  m2[:len(m2)-1] = list(ans)
    m2[:] = list(ans)

def new_matrix(rows):
    m = []
    for r in range(rows):
        m.append([])
        for c in range(cols):
            m[r].append([])
    return m

def new_matrix(rows = 4, cols = 4):
    m = []
    for r in range(rows):
        m.append([])
        for c in range(cols):
            m[r].append( 0 )
    return m

'''m1 = [[1,2,3],[4,5,6],[7,8,9]]
m2 = [[1,2],[3,4],[5,6]]
matrix_mult(m1,m2)
print print_matrix(m2)
ident(m1)
print print_matrix(m1)
m = new_matrix()
print print_matrix(m)
ident(m)
print print_matrix(m)'''
