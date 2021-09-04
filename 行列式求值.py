#初始化
i = int(input("请输入行列式阶数："))
X=[]
sign =1
result = 1
con = True

for r in range(i):
        X.append(list(map(int, input(f"请输入行列式的第{r+1}行：").split(","))))
        
#首元化为非零
def DeZero(row):
    global con,sign
    if X[row][row] == 0:
        con = False
        for r in range(row+1,i):
            if X[r][row] != 0:
                sign *= -1
                X[row],X[r] = X[r],X[row]
                con = True
                break
            
#制造零
def Zero(row):
    for l in range(row+1,i):
        k = X[row][l]/X[row][row]
        for r in range(row+1,i):
            X[r][l] -= X[r][row]*k

#主程序
for r in range(i):
    DeZero(r)
    if con:
        Zero(r)
    else:
        result = 0
        break
    
#打印结果
if result != 0:
    result *= sign
    for r in range(i):
        result *= X[r][r]
    print(f"计算结果：{result}")
else:
    print("计算结果是：0")
    
    
    
    
    
    
