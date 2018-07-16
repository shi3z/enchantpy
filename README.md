# enchant.py
enchant.js like game framework for Python.
This is pre-alpha version.

# Why enchant.js to Python?

![image]('./chara1.png')

We held a programming school for teenager.
But JavaScripts isn't work well in Chromium on Raspberry Pi.

PyGame is great library for coding, but it is pretty difficult to teach how to make a game for kids.

We already have a so many samples and training kits based on enchant.js.


So, we made a enchant.js style framework for Python.
This is it.

So, this framework is not suitable for making a GREAT GAME.


And, python is very good language and environment to make a web services or neural networks.

So,the first purpose of this framework is bridge from JavaScript to Python.
And the second is that open the gate for kids to join a practical programming world.

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


# Licences

MIT Licence

# Reference

https://github.com/wise9/enchant.js/
