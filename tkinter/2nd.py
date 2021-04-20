import tkinter
from tkinter import *
win=Tk()

#menubutton
'''mb =Menubutton(win,text='menu')
mb.grid()
mb.menu=Menu(mb)
mb['menu']=mb.menu

x1=IntVar()
x2=IntVar()

mb.menu.add_checkbutton(label='open',variable='x1')
mb.menu.add_checkbutton(label='close',variable='x2')'''


#menu bar
'''def nothing():
	n=Toplevel(win)
	b=Button(n,text='nothing button')
	b.pack()

mb=Menu(win)

mbar=Menu(mb)
mbar.add_command(label='File',command=nothing)
mbar.add_command(label='New File',command=nothing)
mbar.add_separator()
mbar.add_command(label='open',command=nothing)
mbar.add_command(label='close',command=nothing)
mbar.add_separator()
mbar.add_command(label='exit',command=win.quit)

mb.add_cascade(label="FILE",menu=mbar)
win.config(menu=mb)


#scroll and Spin

s=Scale(win)
s.pack()
sp=Spinbox(win,from_=0,to=10)
sp.pack()
scroll=Scrollbar(win)
scroll.pack(side=RIGHT,fill=Y)
lis=Listbox(win,yscrollcommand=scroll.set)

for line in range(100):
	lis.insert(END,'this line no is'+str(line))

lis.pack(side=LEFT,fill=BOTH)'''

#paned window

p=PanedWindow(win)
p.pack(fill=BOTH,expand=1)

left=Entry(p,bd=5)
p.add(left)

p1=PanedWindow(p,orient=VERTICAL)
p.add(p1)

s=Scale(p1,orient=HORIZONTAL)
p1.add(s)

b=Button(p1,text='Button')
p1.add(b)
win.mainloop()

