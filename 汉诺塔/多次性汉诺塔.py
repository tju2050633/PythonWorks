from tkinter import*

#全局定义
n = 9

window = Tk()
window.title("汉诺塔")
window.geometry("1000x500")

canvas =Canvas(window,width=1000,height=450,bg="white")

line1 = canvas.create_line(197,400,197,200)
line2 = canvas.create_line(497,400,497,200)
line3 = canvas.create_line(797,400,797,200)

canvas.pack()

label1 = Label(window,width=30,height=1,bg="black")
label1.place(x=60,y=400,anchor="nw")

label2 = Label(window,width=30,height=1,bg="black")
label2.place(x=360,y=400,anchor="nw")

label2 = Label(window,width=30,height=1,bg="black")
label2.place(x=660,y=400,anchor="nw")

#创造铁片

piece1 = Label(window,width=27,height=1,bg="orange")
piece1.place(relx=0.2,y=389,anchor="center")

piece2 = Label(window,width=24,height=1,bg="pink")
piece2.place(relx=0.2,y=367,anchor="center")

piece3 = Label(window,width=21,height=1,bg="blue")
piece3.place(relx=0.2,y=345,anchor="center")

piece4 = Label(window,width=18,height=1,bg="green")
piece4.place(relx=0.2,y=323,anchor="center")

piece5 = Label(window,width=15,height=1,bg="purple")
piece5.place(relx=0.2,y=301,anchor="center")

piece6 = Label(window,width=12,height=1,bg="grey")
piece6.place(relx=0.2,y=279,anchor="center")

piece7 = Label(window,width=9,height=1,bg="yellow")
piece7.place(relx=0.2,y=257,anchor="center")

piece8 = Label(window,width=6,height=1,bg="red")
piece8.place(relx=0.2,y=235,anchor="center")

piece9 = Label(window,width=3,height=1,bg="black")
piece9.place(relx=0.2,y=213,anchor="center")

#主程序

def Start1():
    Hanno("line1","line2","line3",n)
def Start2():
    Hanno("line3","line2","line1",n)

    
heap = {"line1":[piece1,piece2,piece3,
               piece4,piece5,piece6,
               piece7,piece8,piece9],
        "line2":[],
        "line3":[]}
location = {"line1":0.2,"line2":0.5,"line3":0.8}
count = {"line1":9,"line2":0,"line3":0}
        
def Hanno(home,support,destination,n):
    if n == 1:
        if count[home] > 0:
            count[home] -= 1
        subject = heap[home].pop()
        window.update()
        for i in range(100000):
            pass
        subject.place(relx=location[destination],
                      y=389-22*count[destination],
                      anchor="center")
        heap[destination].append(subject)
        count[destination] += 1
    else:
        Hanno(home, destination, support, n-1)
        if count[home] > 0:
            count[home] -= 1
        subject = heap[home].pop()
        window.update()
        for i in range(100000):
            pass
        subject.place(relx=location[destination],
                      y=389-22*count[destination],
                      anchor="center")
        heap[destination].append(subject)
        count[destination] += 1
        
        Hanno(support, home, destination, n-1)

button1 = Button(window,width=4,height=2,text="开始修塔！",command=Start1)
button1.place(x=300,y=480,anchor="center")
button2 = Button(window,width=4,height=2,text="归位！",command=Start2)
button2.place(x=600,y=480,anchor="center")

window.mainloop()