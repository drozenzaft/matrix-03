import math


def print_matrix( matrix ):
    s = ""
    for r in matrix:
        for c in r:
            s += c + ' '
        s += '\n'
    print s[:len(s)-2]

def ident( matrix ):
    for r in matrix:
        for c in r:
            if r == c:
                matrix[r][c] = 1
            else:
                matrix[r][c] = 0

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    ans = new_matrix(len(m2), len(m1[0]))
    for r in ans:
        for c in r:
            ans[r][c] 



def new_matrix(rows, cols):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
