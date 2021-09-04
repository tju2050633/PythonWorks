count = 0

def Hanno(home,support,destination,n):
    global count
    if n == 1:
        count += 1
        print(f"{home}>>>{destination}",count)
    else:
        Hanno(home, destination, support, n-1)
        count += 1
        print(f"{home}>>>{destination}",count)
        Hanno(support, home, destination, n-1)
        
Hanno("A","B","C", 30)
        