import tkinter as tk
from tkinter import *
from functools import partial
from tkinter import messagebox
'''#button
win=Tk()
def pr():
	print("hello")
win.geometry("400x500")
b=Button(win,text='button',command=pr,padx=20,pady=10,activeforeground='blue')
b.place(x=200,y=200)

win.mainloop()

#canva
win1=Tk()
c=Canvas(win1,height=400,width=300,bg='red')
cord=20,10,200,300
arc=c.create_arc(cord,start=0,extent=180,fill='yellow')
line=c.create_line(10,20,40,50,fill='white')
c.pack()
win1.mainloop()

#checkbutton and radiobutton
win2=Tk()
c=IntVar()
c1=IntVar()
var=IntVar()
cb=Checkbutton(win2,text='Checkbutton',onvalue=1,offvalue=0,height=3,width=10,variable=c)
cb.pack()
cb1=Checkbutton(win2,text='Checkbutton1',onvalue=1,offvalue=0,height=3,width=10,variable=c1)
cb1.pack()
r1=Radiobutton(win2,text='Radiobutton1',height=3,width=10,value=1,variable=var)
r1.pack()
r2=Radiobutton(win2,text='Radiobutton2',height=3,width=10,value=2,variable=var)
r2.pack()
r3=Radiobutton(win2,text='Radiobutton3',height=3,width=10,value=3,variable=var)
r3.pack()

win2.mainloop()'''
win3=Tk()

def sum(label,x1,x2):
	n1=(x1.get())
	n2=(x2.get())
	sum=int(n1)+int(n2)
	label.config(text='sum is:%d' %sum)

l1=Label(win3,text='enter number 1')
l1.grid(row=1,column=0)
l2=Label(win3,text='enter number 2')
l2.grid(row=2,column=0)
label=Label(win3)
label.grid(row=5,column=2)

x1=StringVar()
x2=StringVar()
e1=Entry(win3,textvariable=x1)
e1.grid(row=1,column=1)
e2=Entry(win3,textvariable=x2)
e2.grid(row=2,column=1)
sum=partial(sum,label,x1,x2)

b=Button(win3,text='calculate',command=sum)
b.grid(row=3,column=0)

win3.mainloop()

'''
#frames
win=Tk()

frame=Frame(win)
frame.pack()
f2=Frame(win)
f2.pack(side=BOTTOM)
b=Button(frame,text='Red',fg='red')
b.pack(side=LEFT)
b1=Button(frame,text='Black',fg='black')
b1.pack(side=RIGHT)
b2=Button(frame,text='blue',fg='blue')
b2.pack(side=RIGHT)
b3=Button(f2,text='green',fg='green')
b3.pack()
win.mainloop()

win3=Tk()
l=Listbox(win3)
l.insert(1,'python')
l.insert(2,'java')
l.insert(3,'c++')
l.insert(4,'c')
l.pack()
win3.mainloop()

win3=Tk()

win3.title('first')
top=Toplevel()
top.title('second')
win3.mainloop()'''

win3=Tk()

def hello():
	messagebox.showinfo('title','message hello')
b=Button(win3,text='pop-up',fg='red',command=hello)
b.pack()
win3.mainloop()