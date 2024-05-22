def data():
    global root
    root.destroy()
    import tkinter as tk
    root=tk.Tk()
    root.title("Enter Data Points")
    canvas=tk.Canvas(root,height=1900,width=1900,bg="white").pack()
    frame=tk.Frame(canvas,bg="yellow")
    frame.place(relheight=0.96,relwidth=0.98,relx=0.01,rely=0.02)
    tk.Label(frame,text="ENTER THE DATA POINTS",font=("algerian",40),bg="yellow").place(x=325,y=100)
    tk.Label(frame,text="X:",font=("algerian",30),bg="yellow").place(x=250,y=200)
    tk.Label(frame,text="Y:",font=("algerian",30),bg="yellow").place(x=750,y=200)
    tk.Label(frame,text="X:",font=("algerian",30),bg="yellow").place(x=250,y=300)
    tk.Label(frame,text="Y:",font=("algerian",30),bg="yellow").place(x=750,y=300)
    tk.Label(frame,text="X:",font=("algerian",30),bg="yellow").place(x=250,y=400)
    tk.Label(frame,text="Y:",font=("algerian",30),bg="yellow").place(x=750,y=400)
    global x1
    global y1
    global x2
    global y2
    global x3
    global y3
    x1=tk.Entry(frame,width=10,font=("algerian",30))
    x1.place(x=300,y=200)
    y1=tk.Entry(frame,width=10,font=("algerian",30))
    y1.place(x=800,y=200)
    x2=tk.Entry(frame,width=10,font=("algerian",30))
    x2.place(x=300,y=300)
    y2=tk.Entry(frame,width=10,font=("algerian",30))
    y2.place(x=800,y=300)
    x3=tk.Entry(frame,width=10,font=("algerian",30))
    x3.place(x=300,y=400)
    y3=tk.Entry(frame,width=10,font=("algerian",30))
    y3.place(x=800,y=400)
    tk.Button(frame,text="FIND THE EQUATION",font=("algerian",30),fg="white",bg="green",command=find).place(x=400,y=500)
def find():
    import csv
    import pandas as pd
    from sklearn.linear_model import LinearRegression
    import numpy as np
    import tkinter as tk
    from matplotlib.figure import Figure
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    f=open("datapoints.csv","w")
    writer=csv.writer(f)
    writer.writerow(["x","y"])
    global x1
    global y1
    global x2
    global y2
    global x3
    global y3
    x1=int(x1.get())
    y1=int(y1.get())
    x2=int(x2.get())
    y2=int(y2.get())
    x3=int(x3.get())
    y3=int(y3.get())
    writer.writerow([x1,y1])
    writer.writerow([x2,y2])
    writer.writerow([x3,y3])
    f.close()
    data=pd.read_csv("C:\Pratheepa\Linear Equation\datapoints.csv")
    X=data["x"]
    Y=data["y"]
    model=LinearRegression()
    X=(np.array(X)).reshape(-1,1)
    model.fit(X,Y)
    global root
    root.destroy()
    root=tk.Tk()
    root.title("The Equation")
    canvas=tk.Canvas(root,height=1900,width=1900,bg="white").pack()
    global frame
    frame=tk.Frame(canvas,bg="yellow")
    frame.place(relheight=0.96,relwidth=0.98,relx=0.01,rely=0.02)
    global a
    global b
    global x
    a="{0:.2f}".format(model.coef_[0])
    b="{0:.2f}".format(model.intercept_)
    tk.Label(text="The equation is y =",font=("arial black",20),bg="yellow").place(x=100,y=100)
    tk.Label(text=a,font=("arial black",20),bg="yellow").place(x=390,y=100)
    tk.Label(text="x +",font=("arial black",20),bg="yellow").place(x=465,y=100)
    tk.Label(text=b,font=("arial black",20),bg="yellow").place(x=520,y=100)
    x=np.linspace(-10,10)
    y=float(a)*x+float(b)
    fig=Figure(figsize=(5,5))
    plt=fig.add_subplot()
    plt.plot(x,y)
    graph=FigureCanvasTkAgg(fig,master=frame)
    graph.draw()
    graph.get_tk_widget().place(x=100,y=150)
    tk.Label(frame,text="DO YOU WANT TO FIND Y FOR ANY GIVEN X?",font=("algerian",20),bg="yellow").place(x=700,y=200)
    tk.Label(frame,text="PLEASE ENTER HERE..",font=("algerian",20),bg="yellow").place(x=800,y=250)
    tk.Label(frame,text="X :",font=("algerian",20),bg="yellow").place(x=800,y=350)
    x=tk.Entry(frame,width=15,font=("algerian",20))
    x.place(x=850,y=350)
    tk.Button(frame,width=10,text="FIND",font=("algerian",20),fg="white",bg="green",command=findy).place(x=850,y=450)
def findy():
    global x
    global a
    global b
    global frame
    xvalue=x.get()
    y=float(a)*float(xvalue)+float(b)
    tk.Label(frame,text="THE VALUE OF Y IS",font=("algerian",20),bg="yellow").place(x=800,y=550)
    tk.Label(frame,text=y,font=("algerian",20),bg="yellow").place(x=1050,y=550)
import tkinter as tk
from PIL import ImageTk, Image
root=tk.Tk()
root.title("Linear Equation Finder")
canvas=tk.Canvas(root,height=1900,width=1900,bg="white").pack()
frame=tk.Frame(canvas,bg="yellow")
frame.place(relheight=0.96,relwidth=0.98,relx=0.01,rely=0.02)
tk.Label(frame,text="LINEAR EQUATION FINDER",font=("arial black",30),bg="yellow").place(x=325,y=100)
tk.Label(frame,text="CONFUSED on what equation it is??",font=("algerian",30),fg="blue",bg="yellow").place(x=150,y=200)
img=Image.open("thinking.jpg")
img=img.resize((200,200))
img=ImageTk.PhotoImage(img)
tk.Label(frame,image=img).place(x=900,y=200)
tk.Label(frame,text="WELL, DON'T WORRY",font=("algerian",30),fg="blue",bg="yellow").place(x=250,y=300)
tk.Button(frame,text="FIND IT OUT HERE",font=("algerian",30),fg="white",bg="green",command=data).place(x=300,y=400)
