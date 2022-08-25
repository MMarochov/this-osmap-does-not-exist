import glob
import os

import cv2

os.makedirs("out_tiles", exist_ok=True)

files = glob.glob(r"input_files\*.tif")

for path in files:
    img = cv2.imread(path, cv2.IMREAD_UNCHANGED)[:, :, :3]

    for i in range(10):
        for j in range(10):
            start_x, start_y = i * 1024, j * 1024
            end_x, end_y = start_x + 1024, start_y + 1024
            tile_img = img[start_y: end_y, start_x: end_x]
            cv2.imwrite(os.path.join("out_tiles", f"{os.path.basename(path).split('.')[0]}_{i}_{j}.png"), tile_img)
