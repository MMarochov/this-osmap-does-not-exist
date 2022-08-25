import glob
import os

import cv2

os.makedirs("out_tiles_smaller", exist_ok=True)
for file in glob.glob("out_tiles/*.png"):
    im = cv2.imread(file)
    im = cv2.resize(im, (256, 256))
    cv2.imwrite(os.path.join("out_tiles_smaller", os.path.basename(file)), im)
