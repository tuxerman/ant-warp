#! /usr/bin/python

""" 
	the ant.
    	-SP
"""

import pygame,random

#tuneable parameters
Pfwd=0.7			# probability that ant goes straight
antItchyFeet=7			# number of steps after which ant feels like turning: lesser this is, more influence Pfwd has
antSpeedMpy=2			# multiplier for speed of ant
screenHeight=400		# screen height in px
screenWidth=400			# screen width in px
numAnts=30			# number of ants
floorColour = (220,220,200)	# colour of the floor - (R,G,B), 0-256
antColour = (90,0,0)		# colour of ants - (R,G,B), 0-256

#DO NOT change these variables
dirs=[1,2,3,4,5,6,7,8]
dirX={1:0,2:1,3:1,4:1,5:0,6:-1,7:-1,8:-1}
dirY={1:-1,2:-1,3:0,4:1,5:1,6:1,7:0,8:-1}
Pside=Pfwd+(1-Pfwd)/2

##### CODE BEGINS #####

def getglobals():
	#input parameter values to override the ones in the file
	#TODO add command-line initialisation
	pass
	
#Randomly return one item out of many in the list
def chooseOne(item_list):
	rnd_index=random.uniform(0,len(item_list))
	return item_list[int(rnd_index)]

#Is the ant on the edge of the screen?
def isOnEdge(pos):
	return (pos[0]<=0 or pos[0]>=screenWidth or pos[1]<=0 or pos[1]>=screenHeight)

def drawAnt(antObj):
	posX=antObj.pos[0]-dirX[antObj.direc]*2
	posY=antObj.pos[1]-dirY[antObj.direc]*2
	pygame.draw.line(screen,antColour,a[n].pos,[posX,posY],2)

class Ant:
	pos=list()
	prev_pos=list()
	def __init__(self,pos,direc,odo=0):
		self.pos=pos
		self.direc=direc
		self.odo=odo

	def update_pos(self):
		#consider edges now:'
		if (self.pos[0]<=0):
			if(self.direc in [8,1]):
				self.direc=chooseOne([1,2])
			elif(self.direc in [6,5]):
				self.direc=chooseOne([5,4])
			else:
				self.direc=chooseOne([1,5])
			self.pos[0]=0
		elif(self.pos[0]>=screenWidth):
			if(self.direc in [2,1]):
				self.direc=chooseOne([1,8])
			elif(self.direc in [4,5]):
				self.direc=chooseOne([6,4])
			else:
				self.direc=chooseOne([1,5])
			self.pos[0]=screenWidth
		if (self.pos[1]<=0):
			if(self.direc in [2,3]):
				self.direc=chooseOne([3,4])
			elif(self.direc in [8,7]):
				self.direc=chooseOne([6,7])
			else:
				self.direc=chooseOne([3,7])
			self.pos[1]=0
		elif(self.pos[1]>=screenHeight):
			if(self.direc in [4,3]):
				self.direc=chooseOne([3,2])
			elif(self.direc in [6,7]):
				self.direc=chooseOne([8,7])
			else:
				self.direc=chooseOne([3,7])
			self.pos[1]=screenHeight

		prob=random.uniform(0,1)
		#change direc
		''' OLD CODE
		if(prob>=Pfwd and prob<=Pside and self.odo>=antItchyFeet):	   
			if(self.direc==1 and self.odo>=antItchyFeet):
				self.direc=8
			elif(self.odo>=antItchyFeet):
				self.direc=self.direc-1 #lean leftward
				self.odo=0
		elif(prob>Pside and self.odo>=antItchyFeet):
			if(self.direc==8 and self.odo>=antItchyFeet):
				self.direc=1
			elif(self.odo>=antItchyFeet):
				self.direc=self.direc+1 #lean rightward
	      			self.odo=0
		else:
			pass #keep going straight'''

		if(self.odo >= antItchyFeet and prob>=Pfwd):
			d1, d2 = self.direc-1, self.direc+1
			self.direc=chooseOne([d1,d2])	#lean left or right
			if(self.direc==0):		#wrap around direction numbers
				self.direc=8
			elif(self.direc==9):
				self.direc=1
			self.odo=0	#reset odometer
		else:
			pass		#keep going
			
		#print self.direc - probe point
		#now move the ant
		self.pos[0]=self.pos[0]+dirX[self.direc]*antSpeedMpy
		self.pos[1]=self.pos[1]+dirY[self.direc]*antSpeedMpy
		self.odo=self.odo+1
		#print self.pos - probe point




getglobals() 
a=list()
for n in range(numAnts):
	px=int(random.uniform(0,screenWidth))
	py=int(random.uniform(0,screenHeight))
	d=int(random.uniform(1,8))
	od=int(random.uniform(0,antItchyFeet))
	a.append(Ant([px,py],d,od))

pygame.init() 
size=[screenWidth,screenHeight] 
screen=pygame.display.set_mode(size) 
pygame.display.set_caption("Ants") 
done=False

clock=pygame.time.Clock() 

while done==False: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True 
    screen.fill(floorColour) 
  
    # Code to draw stuff begins 
    for n in range(numAnts):
    	a[n].update_pos()
	drawAnt(a[n])
    # Drawing-code ends 
      
    clock.tick(20) #FPS
    pygame.display.flip() 

pygame.quit() 


if __name__ == '__main__':
   main()
