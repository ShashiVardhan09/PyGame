import tkinter
from tkinter import font
from tkinter import *
win=Tk()
win.geometry('200x300')
board=[' 'for x in range(10)]
def placepos1():
	if board[1]==' ':
		b1['text']='X'
		board[1]='X'
		def compmove():
	elif:
		board[1]=='O':
		b1['text']='O'
	else:
		l=Label(win,text='Not Valid pos')
		l.grid(row=5,columnspan=3)
def placepos2():
	if board[2]==' ':
		b2['text']=letter
		board[2]=letter
def placepos3():
	if board[3]==' ':
		b3['text']=letter
		board[3]=letter
def placepos4():
	if board[4]==' ':
		b4['text']=letter
		board[4]=letter
def placepos5():
	if board[5]==' ':
		b5['text']=letter
		board[5]=letter
def placepos6():
	if board[6]==' ':
		b6['text']=letter
		board[6]=letter
def placepos7():
	if board[7]==' ':
		b7['text']=letter
		board[7]=letter
def placepos8():
	if board[8]==' ':
		b8['text']=letter
		board[8]=letter
def placepos9():
	if board[9]==' ':
		b9['text']=letter
		board[9]=letter

label=Label(win,text="WElCOME!",font='helv36')
label.grid(row=0,columnspan=3)
b1=Button(win,text=' ',font='helv36',padx=20,pady=30,command=placepos1)
b1.grid(row=1,column=0)
b2=Button(win,font='helv36',padx=20,pady=30,command=placepos2)
b2.grid(row=1,column=1)
b3=Button(win,font='helv36',padx=20,pady=30,command=placepos3)
b3.grid(row=1,column=2)
b4=Button(win,font='helv36',padx=20,pady=30,command=placepos4)
b4.grid(row=2,column=0)
b5=Button(win,font='helv36',padx=20,pady=30,command=placepos5)
b5.grid(row=2,column=1)
b6=Button(win,font='helv36',padx=20,pady=30,command=placepos6)
b6.grid(row=2,column=2)
b7=Button(win,font='helv36',padx=20,pady=30,command=placepos7)
b7.grid(row=3,column=0)
b8=Button(win,font='helv36',padx=20,pady=30,command=placepos8)
b8.grid(row=3,column=1)
b9=Button(win,font='helv36',padx=20,pady=30,command=placepos9)
b9.grid(row=3,column=2)



win.mainloop()