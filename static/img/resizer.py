import os
import sys
import numpy as np
import pandas as pd
import csv
from PIL import Image

pref = 't'
q = 50
res = 300
#ps = ['bar', 'closet', 'commercial', 'fireplace', 'modern', 'other', 'traditional', 'transitional', 'vanities']
for p in ps:
    os.chdir(p)
    n = 1
    fs = os.listdir()
    os.mkdir(pref)
    for f in fs:
        try:
            im = Image.open(f)
            (w, h) = (res, int((im.height * (res / im.width)) // 1))
            im_new = im.resize((w, h))
            im_new.save(pref + '/' + f, 'jpeg', quality=q)
        except:
            pass
    os.chdir('../..')