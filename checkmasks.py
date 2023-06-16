import os, pdb
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

imgs = os.listdir('./')
imgs.sort()
for fname in imgs:
    pdb.set_trace()
    img = Image.open(f'./{fname}')
    img = np.array(img.convert('L'))
    img[img>50]= 255
    img[img<=50]= 0
    
    Image.fromarray(img).save(f'./{fname}')
