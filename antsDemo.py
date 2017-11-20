#Greg Phillips
#11/20/17
#antsDemo.py - how to use lists with graphics

from ggmae import *

if __name__ == "__main__":
    
    red = Color(0xff0000,1)
    ant = CircleAsset(10,LineStyle(1,red),red)
    
    Sprite(ant,50,50)
    
    App().run()
    
    
