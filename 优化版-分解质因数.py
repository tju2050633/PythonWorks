num = int(input("输入一个整数："))
output = str(num)+"="

factor = 2
while factor <= num:
    while num%factor != 0 :
        factor += 1
    num = num/factor
    output += str(factor)+"*"
    factor = 2

print(output[:-1])