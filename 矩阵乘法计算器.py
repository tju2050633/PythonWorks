i = int(input("输入左边矩阵的行数："))
j = int(input("输入左边矩阵的列数（同时也是右边矩阵的行数）："))
k = int(input("输入右边矩阵的列数："))

def show(matrix):
    """漂亮地展示矩阵"""
    print("结果矩阵：")
    for row in matrix:
        for item in row:
            print(item,end=" ")
        print("")
    print("")

X=[]
Y=[]
def define(M,i,m):
    for r in range(i):
        M.append(list(map(int, input(f"请输入{m}的第{r+1}行：").split(","))))
    
define(X,i,"X")
define(Y,j,"Y")
    

    
Z = [[sum([X[i][j]*Y[j][k] for j in range(j)]) for k in range(k)] for i in range(i)]

show(Z)