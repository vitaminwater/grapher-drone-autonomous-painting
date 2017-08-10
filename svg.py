from turtle import *

import time
import sys
import os
import json
import numpy as np
from svgpathtools import svg2paths

import requests

if len(sys.argv) != 2:
    print('Usage: %s nounproject_id' % (sys.argv[0]))
    exit()

TMP_FILE='/tmp/tmp.svg'

import secret

endpoint = 'https://thenounproject.com/icon/%s/download/' % (sys.argv[1])
cookies={'sessionid': secret.sessionid, 'csrftoken': secret.csrftoken}
headers={'X-CSRFToken': secret.csrftoken, 'Origin': 'https://thenounproject.com', 'Referer': 'https://thenounproject.com/'}
response = requests.post(endpoint, cookies=cookies, headers=headers)
response = json.loads(response.content)
icon = requests.get(response['download'], cookies=cookies, headers=headers)
f = open(TMP_FILE, 'w')
f.write(icon.content)  # python will convert \n to os.linesep
f.close()

paths, attributes = svg2paths(TMP_FILE)

os.remove(TMP_FILE)

time.sleep(2)

color('red')

def get_frame(paths):
    x = sys.maxint
    y = sys.maxint
    width = -sys.maxint
    height = -sys.maxint
    for _, path in enumerate(paths):
        for step in np.arange(0.0,1.01,0.01):
            p = path.point(step)
            x = min(x, p.real)
            y = min(y, p.imag)
            width = max(width, p.real)
            height = max(height, p.imag)
    width -= x
    height -= y
    return (x, y, width, height)

def draw_paths(paths, size):
    frame = get_frame(paths)
    ratio = frame[3]/frame[2]
    print(frame)

    def goto_point(seg, step):
        p = seg.point(step)
        x = (((p.real - frame[0]) / frame[2]) * size - size / 2) / ratio
        y = -((p.imag - frame[1]) / frame[3]) * size + size / 2
        goto(x, y)

    for _, path in enumerate(paths):
        # list path points
        for seg in path:
            penup()
            length = seg.length()
            if length == 0: continue
            for step in np.arange(0.0,1.0,1/length):
                goto_point(seg, step)
                if step == 0:
                    pendown()
            goto_point(seg, 1)
    done()

draw_paths(paths, 400)
