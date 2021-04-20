import json
import time
import random
import tkinter 
from tkinter import *
#x=get_close_matches(x,data.keys())
class wordgen(object):
	def __init__(self):
		self.data=json.load(open('data.json'))
		self.dkeys=list(self.data.keys())
		self.word0=random.choice(self.dkeys)
		print(self.word0)
		self.mean=self.data[self.word0]
		self.mean=self.mean[0]
		print(self.mean)
		
		
		self.jword=random.sample(self.word0,len(self.word0))
		self.jword=''.join(self.jword).replace(" ","")
		print(self.jword)
		self.c=5



def tkinterwin():


	def clic():	
		label.config(text="WOrd MEans : \n"+str(word.mean))

	def ent():
		x1=a.get()
		note.config(text="You have "+str(word.c-1)+ " chances to Guess")
		if x1==word.word0:
			lab.config(text='WIN')
		elif x1!=word.word0:
			word.c-=1
			if word.c==0:
				screen.destroy()
	


	word=wordgen()
	screen=Tk()
	screen.geometry('400x400')
	a=StringVar()
	welcome=Label(screen,text="Hello WElcome to GuEss the wORd!")
	welcome.grid(row=0,columnspan=2)


	note=Label(screen)
	note.grid(row=1,column=0)


	l=Label(screen,text="Guess the word :  "+str(word.jword))
	entery=Entry(screen,textvariable=a)
	entery.grid(row=3,column=0)
	l.grid(row=2,column=0)
	
	timeup=Label(screen)
	timeup.grid(row=10,column=0)
	

	lab=Label(screen)
	lab.grid(row=8,column=0)
	b=Button(screen,text="Submit",command=ent)
	b.grid(row=4,column=0)

	label=Label(screen)
	label.grid(row=7,column=0)

	hint=Button(screen,text="Hint",command=clic)
	hint.grid(row=6,column=0)

	
	
	screen.mainloop()
tkinterwin()