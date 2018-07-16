# enchant.py
enchant.js like game framework for Python.
Alpha version

# Requirements

- PyGame

# Usage

~~~
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
~~~

# Limitation of this version

- Only Sprite,Label and Scene,Game classes support
- You can handle bellow events
  - ENTERFRAME
  - TOUCHSTART
  - TOUCHEND
  - TOUCHMOVE
- Not supported below classes
  - MAP
- Not supported any plugins
  - Ex. timelines,OpenGL,Physics,etc.
