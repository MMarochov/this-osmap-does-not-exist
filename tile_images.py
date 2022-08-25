import cv2 

path = r"C:\Users\MMarochov\Documents\RPT\Mapnt\data\tv\TV49.tif"
img = cv2.imread(path, cv2.IMREAD_UNCHANGED)

print(img.shape)
