#Greg Phillips
#9/16/17
#betColWin.py

from random import randint
from ggame import *

color = ["0xFF0000","0x00FF00","0x0000FF"]

def mouseClick(event):
    num = randint(1,3)
    colors = Color(color[num-1],1)

    Rect = RectangleAsset(1000, 1000, LineStyle(1, colors), colors)
    Sprite(Rect)
        

        
App().listenMouseEvent("click", mouseClick)
App().run()
