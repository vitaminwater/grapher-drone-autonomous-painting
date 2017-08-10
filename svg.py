from turtle import *

import numpy as np
from svgpathtools import svg2paths

paths, attributes = svg2paths('smiley.svg')

color('red')
for _, path in enumerate(paths):
    # list path points
    for seg in path:
        penup()
        for step in np.arange(0.0,1.0,1/seg.length()):
            p = seg.point(step)
            goto(p.real * 3 - 200, -p.imag * 3 + 200)
            if step == 0:
                pendown()
done()
