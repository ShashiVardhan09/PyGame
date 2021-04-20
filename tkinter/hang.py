import time
import pygame
import json
import random
import tkinter 
from tkinter import *
pygame.init()
win = pygame.display.set_mode((481,284))
walk_man = [pygame.image.load('character/R1.png'),pygame.image.load('character/R2.png'),pygame.image.load('character/R3.png'),pygame.image.load('character/R4.png'),pygame.image.load('character/R5.png'),pygame.image.load('character/R6.png'),pygame.image.load('character/R7.png'),pygame.image.load('character/R8.png'),pygame.image.load('character/R9.png')]
pygame.display.set_caption("Guess_Game")
bg=pygame.image.load('bg1.jpg').convert()
guess=pygame.image.load('guess.png')

#random word generation 
class wordgen(object):
	def __init__(self):
		self.data=json.load(open('data.json'))
		self.dkeys=list(self.data.keys())
		self.word0=random.choice(self.dkeys)
		print(self.word0)
		self.mean=self.data[self.word0]
		self.mean=self.mean[0]
		print(self.mean)
		self.run=False
		
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
				wordgen.run=True
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


class charc(object):
	def __init__(self,x,y):
		self.x=x
		self.y=y
		self.walk_count=0
		self.iswalk=False
		self.vel=5
		self.right=True
		self.standing=True
		self.downfall=False
		self.clock=pygame.time.Clock()


	def drawcharc(self,win):
		if (self.standing):
			win.blit(walk_man[0],(self.x,self.y))
		else:
			if self.walk_count>=9:
				self.walk_count=0
			if True:			
				win.blit(walk_man[(self.walk_count)],(self.x,self.y))
				self.walk_count+=1
			if self.downfall:
				win.blit(walk_man[0],(self.x,self.y))





def windraw():
	win.blit(bg,(0,0))
	win.blit(guess,(180,0))
	#wordbox=makeTextBox(10,10,300,0,"enter ",0,24
	man.drawcharc(win)
	pygame.display.update()

def dline():
	pygame.draw.line(win,(0,0,0),(300,200),(300,0))


#main loop
pos=[]
man=charc(0,111)
man1=charc(0,0)
while wordgen.run:


	man.clock.tick(27)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			wordgen.run = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			pos.append(pygame.mouse.get_pos())
			print(pos)
			
	keys=pygame.key.get_pressed()
	

	if True and man.x<350:
		pygame.time.wait(50)
		man.x+=man.vel
		if man.x>100 and man.x<330:
			man.y=120
		man.iswalk=True
		man.standing=False
		man.downfall=False
	
	if  man.x>340 and man.y<250:
		pygame.time.wait(100)
		man.y+=man.vel
		man.downfall=True
		man.right=False
		man.standing=True
		
	
	windraw()
				
pygame.quit()