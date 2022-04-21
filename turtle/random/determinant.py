
'''
def det(mat):
    if len(mat) != len(mat[0]): return ValueError
'''
'''
    for i in mat:
        for k in mat:
            if k == i: return 0
'''
'''
    if len(mat) == 2: return mat[0][0]*mat[1][1] - mat[0][1]*mat[1][0]
    s = 0
    for a,i in enumerate(mat[0]):
        m = [mat[i].copy() for i in range(len(mat))]
        m.remove(m[0])
        for i in range(2): m[i].remove(m[i][a])
        s += i*det(m) if a%2==0 else -i*det(m)
    return s
'''

def det(mat):
    if len(mat) != len(mat[0]): return ValueError
    if len(mat) == 2: return mat[0][0]*mat[1][1] - mat[0][1]*mat[1][0]
    s = 0
    for a,i in enumerate(mat[0]):
        m = [mat[k].copy() for k in range(1,len(mat))]
        for j in range(len(mat) - 1): m[j].pop(a)
        s += i*det(m) if a%2==0 else -i*det(m)
    return s

'''
def minor(mat):
    m = [mat[k].copy() for k in range(1,len(mat))]
    for a,i in enumerate(mat):
        for b,k in enumerate(i):
'''

def adj(mat):
    m = [mat[k].copy() for k in range(len(mat))]
    if len(m) != len(m[0]): return ValueError
    if len(m) == 2:
        m[0][0], m[1][1], m[0][1], m[1][0] = m[1][1], m[0][0], -m[0][1], -m[1][0]
        return m
    
        

#a, b, c = 1, 1, 1

'''
matrix = [[7, 8, 7],
          [8, 7, 8],
          [7, 1, 7]]

'''
'''
matrix = [[7, 8, 7,-7],
          [8, 7, 8,-1],
          [2,-4, 1, 1],
          [7, 1, 7,-4]]
'''
matrix = [[8, 3],
          [8, 7]]

#print("The determinant is",det(matrix))
print("The adjacent is",adj(matrix))
print(matrix)


