#初始化
i = int(input("请输入行列式阶数："))
X=[]
Y=[]
for r in range(i):
    Y.append([1]*i)

for r in range(i):
        X.append(list(map(int, input(f"请输入行列式的第{r+1}行：").split(","))))

X_copy = X[:]   #用替身求伴随矩阵吧

#求X的行列式result
def Value(M,n):
    i = n
    sign = 1
    result = 1
    con = True
    
    def DeZero(row):
        nonlocal con,sign
        if M[row][row] == 0:
            con = False
            for r in range(row+1,i):
                if M[r][row] != 0:
                    sign *= -1
                    M[row],M[r] = M[r],M[row]
                    con = True
                    break
            
    def Zero(row):
        for l in range(row+1,i):
            k = M[row][l]/M[row][row]
            for r in range(row+1,i):
                M[r][l] -= M[r][row]*k
                        
    for r in range(i):
        DeZero(r)
        if con:
            Zero(r)
        else:
            result = 0
            break
    
    if result != 0:
        result *= sign
        for r in range(i):
            result *= M[r][r]
    else:
        result = 0
            
    return result
            
result = Value(X,i)

#求X的伴随矩阵Y

def AlgebraicCodial(r,l):
    """求代数余子式"""
    temp = X_copy[:]
    temp.pop(r)
    
    for row in range(i-1):
        temp[row].pop(l)
    
    return (-1)**(r+l)*Value(temp,i-1)
        
for r in range(i):
    for l in range(i):
        Y[l][r] = AlgebraicCodial(r, l)

#处理伴随矩阵，计算出逆矩阵Y
for r in Y:
    for l in Y:
        Y[r][l] /= result

#漂亮地打印Y
for r in Y:
    for l in Y[r]:
        print(Y[r][l],end=" ")
    print("")