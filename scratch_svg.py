import random
import os
import sys
import xlsxwriter
import pandas as pd
import drawSvg as draw
from datetime import date



ySize = 350
xSize = 380

emSize = 12


d = draw.Drawing(xSize, ySize, origin=(0,0), displayInline=False)

box2 = draw.Rectangle(0, 0, xSize, ySize,
    fill='#ffffff',stroke_width=2,stroke='red')
d.append(box2)

box1 = draw.Rectangle(0, 10, 20, 30,
    fill='#ffffff',stroke_width=2,stroke='black')
d.append(box1)




groupLabel = draw.Text('Hello World',
                12,
                50,60,
                fill='black')
d.append(groupLabel)

box1 = draw.Rectangle(50, 60, 80, emSize,
    fill='none',stroke_width=2,stroke='black')
d.append(box1)

filename = 'test_' + '1' + '.svg'

d.saveSvg(filename)
os.system('/Applications/Inkscape.app/Contents/MacOS/inkscape ' + filename + ' -o ' + filename + '.png')
