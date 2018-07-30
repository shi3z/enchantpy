# -*- coding: utf-8 -*-
from __future__ import print_function
import pygame
from pygame.locals import *
import sys
import inspect
 




class Entity:
	list=[]
	classList={}
	button=False
	def __init__(self):
		self.x=0
		self.y=0
		self.w=0
		self.h=0
		self.listeners=[]
		self.children=[]
		self.born=Game.age
		Entity.list.append(self)
		if not hasattr(Entity.classList,self.__class__.__name__):
			Entity.classList[self.__class__.__name__]=[]
		Entity.classList[self.__class__.__name__].append(self)

	def __getattr__(self,name):
		if name=="age":
			return Game.age-self.__dict__['born']

		raise AttributeError

	def addChild(self,child):
		self.children.append(child)

	def removeChild(self,child):
		if child in self.children:
			self.children.remove(child)
		if child in Entity.list:
			Entity.list.remove(child)
		#Entity.classList[self.__class__.__name__].remove(child)

	def addEventListener(self,event,func,type='external'):
		self.listeners.append({'event':event,'handler':func,'type':type})

	def dispatchEvent(self,eventtype,event):
		if hasattr(event,'pos'):
			x,y = event.pos
			if (self.x <= x and x <= self.x+self.w and
			   self.y <= y and y <= self.y+self.h ):
			   	pass
			else:
				return
			
		for listener in self.listeners:
			if eventtype == listener['event']:
				if listener['type']=='external':
					listener['handler'](event,target=self)
				else:
					listener['handler'](event)

	def intersect(self,classObj):
		if classObj.__name__ in Entity.classList:
			r = []
			for t in Entity.classList[classObj.__name__]:
				if (t.x <= self.x+self.w and self.x <=t.x+t.w and
					t.y <= self.y+self.h and self.y <=t.y+t.h):
					r.append(t)
			return r
		return []

	def hit(self,classObj):
		if len(self.intersect(classObj))>0:
			return True
		return False

	@staticmethod 
	def postEvent(event):
		eventtype=None
		if type(event) is str:
			eventtype=event
		else:
			if hasattr(event,'pos'):
				event.x = event.pos[0]
				event.y = event.pos[1]
			if event.type == MOUSEBUTTONDOWN:
				eventtype='touchstart'
				Entity.button = True
			if event.type == MOUSEBUTTONUP:
				eventtype='touchend'
				Entity.button = False
			if event.type == MOUSEMOTION:
				if Entity.button:
					eventtype='touchmove'
		for entity in Entity.list:
			entity.dispatchEvent(eventtype,event)

	def _reset(self):
		pass
	def _draw(self,_):
		pass

	@staticmethod 
	def init():
		for entity in Entity.list:
			entity._reset()

class Label(Entity):
	def __init__(self,text):
		Entity.__init__(self)
		self.text=text
		self.size = 32
		self.font = pygame.font.Font(None,self.size)
		self.color = (255,255,255)
		self.label = self.font.render(self.text, 1, self.color)
		self.x = 0
		self.y = 0
		self.initialized=True

	def _draw(self,screen):
		screen.blit(self.label, (self.x, self.y))

	def __setattr__(self,name,value):
		self.__dict__[name] = value
		if not hasattr(self,'initialized'):
			return
		if name=='text':
			self.label = self.font.render(self.text, 1, self.color)
		if name=='size':
			self.font = pygame.font.Font(None,self.size)

class Sprite(Entity):
	def __init__(self,imageFile,w,h):
		Entity.__init__(self)
		self.img = pygame.image.load(imageFile).convert_alpha()
		self.img_rect = self.img.get_rect()
		self._frameWidth = self.img_rect[2]//w
		self.w=w
		self.h=h
		self.scaleX=1
		self.scaleY=1
		self.frame=0
		self.initialized=True
		self._updateScale()
		self._updateArea()
		self._reset()

	def __setattr__(self,name,value):
		self.__dict__[name] = value
		if not hasattr(self,'initialized'):
			return
		if name=='frame':
			self._updateArea()
		if name=='scaleX' or name=='scaleY':
			self._updateScale()

	def _updateScale(self):
		self.img=pygame.transform.scale(self.img,
					(self.scaleX*self.img_rect[2],self.scaleY*self.img_rect[3]))

	def _updateArea(self):

		x = self.frame % self._frameWidth;
		y = self.frame // self._frameWidth;


		self.area = pygame.Rect(x*self.w*self.scaleX,y*self.h*self.scaleY,
								self.w*self.scaleX,self.h*self.scaleY)

	def _draw(self,screen):
		screen.blit(self.img, (self.x,self.y,
								self.x+self.w*2,self.y+self.h*2),area=self.area)

	def _reset(self):
		for x in inspect.getmembers(self, inspect.ismethod):
			if x[0][0:2]=='on':
				self.addEventListener(x[0][2:],x[1],type='internal')

class Scene(Entity):
	def __init__(self,w,h):
		Entity.__init__(self)
		self.w=w
		self.h=h
		self.canvas=False
		SCREEN_SIZE = (w, h)
		self.color=(0,0,255) 
		pygame.init()
		self.screen = pygame.display.set_mode(SCREEN_SIZE)

	def draw(self):
		if self.canvas == False:
			self.screen.fill(self.color)
		for entity in self.children:
			entity._draw(self.screen)

class Pad:
		up = False
		left = False
		right = False
		down = False
		space = False

class Game:
	age=0
	FPS=30
	def __init__(self,w,h):
		self.rootScene = Scene(w,h)
		self.input=Pad()

	def start(self):
		Entity.init()

		clock = pygame.time.Clock()
		while True:
			Game.age +=1
			self.rootScene.draw()

			pygame.event.pump() #おまじない
			pressed = pygame.key.get_pressed()

			clock.tick_busy_loop(Game.FPS)
			pygame.display.update()


			pressed_keys = pygame.key.get_pressed()


			if pressed_keys[K_ESCAPE]:
				sys.exit()

			self.input.up 		= pressed_keys[K_UP]
			self.input.down 	= pressed_keys[K_DOWN]
			self.input.left 	= pressed_keys[K_LEFT]
			self.input.right 	= pressed_keys[K_RIGHT]
			self.input.space 	= pressed_keys[K_SPACE]
			self.input.all 	= pressed_keys

			for event in pygame.event.get():
				Entity.postEvent(event)
			Entity.postEvent('enterframe')

pygame.init()
