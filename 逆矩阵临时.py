#初始化
order = int(input("请输入行列式阶数："))
X=[]
Y=[]
for r in range(order):
    Y.append([1]*order)

for r in range(order):
        X.append(list(map(int, input(f"请输入行列式的第{r+1}行：").split(","))))

X_copy = X[:]   #用替身求伴随矩阵吧

#求X的行列式result
def Value(M,n):
    sign = 1
    result = 1
    con = True
    
    def DeZero(row):
        nonlocal con,sign,n
        if M[row][row] == 0:
            con = False
            for r in range(row+1,n):
                if M[r][row] != 0:
                    sign *= -1
                    M[row],M[r] = M[r],M[row]
                    con = True
                    break
            
    def Zero(row):
        nonlocal n
        for l in range(row+1,n):
            k = M[row][l]/M[row][row]
            for r in range(row+1,n):
                M[r][l] -= M[r][row]*k
                        
    for r in range(n):
        DeZero(r)
        if con:
            Zero(r)
        else:
            result = 0
            break
    
    if result != 0:
        result *= sign
        for r in range(n):
            result *= M[r][r]
    else:
        result = 0
            
    return result
            
result = Value(X,order)

#求X的伴随矩阵Y

def AlgebraicCodial(r,l):
    """求代数余子式"""
    temp = X_copy[:]
    temp.pop(r)
    
    for row in range(order-1):
        temp[row].pop(l)
    
    return (-1)**(r+l)*Value(temp,order-1)
        
for r in range(order):
    for l in range(order):
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