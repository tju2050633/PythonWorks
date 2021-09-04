X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9],
    [1,2,3]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9],
    [2,3,4]]

Z=[[X[j][i]+Y[j][i] for i in range(3)] for j in range(4)]

def show(matrix):
    """漂亮地展示矩阵"""
    for row in matrix:
        for item in row:
            print(item,end=" ")
        print("")
    print("")
    
show(X)
show(Y)
show(Z)