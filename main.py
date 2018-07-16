# -*- coding: utf-8 -*-
from enchant import *

class Kuma(Sprite):
	def __init__(self):
		Sprite.__init__(self,"chara1.png",32,32)
	def onenterframe(self,e):
		self.frame=self.age//4%3

class Apple(Sprite):
	def __init__(self):
		Sprite.__init__(self,"icon0.png",16,16)
		self.frame=15
	def onenterframe(self,e):
		global score
		if self.hit(Kuma)>0:
			game.rootScene.removeChild(self)
			score+=1
			scoreLabel.text="Score:%d" % score

score=0
scoreLabel = Label("Score:0")

game = Game(640,480)
kuma = Kuma()
import random
for i in range(10):
	fruits=Apple()
	fruits.x=random.randint(0,600)
	fruits.y=random.randint(0,400)
	game.rootScene.addChild(fruits)

def kumamove(e):
	kuma.x = e.x
	kuma.y = e.y

def moveLeft(e,target):
	target.x += 10


def keyhandler(e,target):
	if game.input.left:
		kuma.x -= 8
	if game.input.right:
		kuma.x += 8
	if game.input.up:
		kuma.y -= 8
	if game.input.down:
		kuma.y += 8
	if game.input.space:
		tama = Apple()
		tama.x = kuma.x
		tama.y = kuma.y
		tama.addEventListener('enterframe',moveLeft)
		game.rootScene.addChild(tama)



game.rootScene.addChild(kuma)
game.rootScene.addChild(scoreLabel)
game.rootScene.addEventListener('touchmove',kumamove)
game.rootScene.addEventListener('enterframe',keyhandler)
game.start()

