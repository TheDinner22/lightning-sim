# this could and will be better i just needed to make it here as a 
# proof of concept but it will be online and better later

import os, sys

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # adds project dir to places it looks for the modules
sys.path.append(BASE_PATH)

from lib.board import Board
from lib.window import Window

b = Board()
win = Window(b)

win.main()