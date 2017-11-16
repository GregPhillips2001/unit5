#Greg Phillips
#9/16/17
#betColWin.py

from random import randint
from ggame import *

color = ["Color(0xFF0000, 1)","Color(0x00FF00, 1)","Color(0x0000FF, 1)"

def mouseClick(event):
    num = randint(1,3)
    
    if num == 1:
        red = Color(0xFF0000, 1)
        redRect = RectangleAsset(1000, 1000, LineStyle(1, red), red)
        Sprite(redRect)
        
    elif num == 2:
        green = Color(0x00FF00, 1)
        greenRect = RectangleAsset(1000, 1000, LineStyle(1, green), green)
        Sprite(greenRect)

    else:
        blue = Color(0x0000FF, 1)
        blueRect = RectangleAsset(1000, 1000, LineStyle(1, blue), blue)
        Sprite(blueRect)

        
App().listenMouseEvent("click", mouseClick)
App().run()
