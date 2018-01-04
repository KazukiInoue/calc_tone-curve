import numpy as np
import cv2

src = cv2.imread("./input_images/edited.jpg", cv2.IMREAD_UNCHANGED)
print("shape = {}".format(src.shape))
# src = cv2.resize(src, fx=0.5, fy=0.5)
src = cv2.resize(src,(256, 256))
cv2.imshow('with alpha channel', src)
cv2.waitKey(0)