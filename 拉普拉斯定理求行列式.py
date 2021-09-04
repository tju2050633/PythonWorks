"""

拉普拉斯展开法求行列式

"""
#初始化
order = int(input("请输入行列式阶数："))
X = [list(map(float, input(f"请输入第{r}行:").split(","))) for r in range(1,order+1)]

#获取代数余子式

def Child(M,l,n):
    child = M[:]
    for r in range(n):
        child[r].pop(l)
    child.pop(0)
        
    return child

#主体函数
def main(M,n):
    if n == 2:
        return M[0][0]*M[1][1] - M[0][1]*M[1][0]
    
    if n > 2:
        result = 0
        for l in range(n):
            result += (-1)**l*main(Child(M,l,n),n-1)
    
        return result
#打印
print("计算结果：",main(X, order))