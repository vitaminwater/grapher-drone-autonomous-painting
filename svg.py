from turtle import *

import numpy as np
from svgpathtools import svg2paths

paths, attributes = svg2paths('smiley.svg')

color('red', 'yellow')
begin_fill()
for _, path in enumerate(paths):
    # list path points
    for step in np.arange(0.0,1.0,0.01):
        p = path.point(step)
        print(p.real, p.imag)
        goto(p.real, -p.imag)
end_fill()
done()
