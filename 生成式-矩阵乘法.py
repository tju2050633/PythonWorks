X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9],
    [1,2,3]]

Y = [[5,8,1,2,1],
    [6,7,3,3,2],
    [4,5,9,4,3]]
    

def show(matrix):
    """漂亮地展示矩阵"""
    for row in matrix:
        for item in row:
            print(item,end=" ")
        print("")
    print("")
    
Z = [[sum([X[i][j]*Y[j][k] for j in range(3)]) for k in range(5)] for i in range(4)]

show(Z)