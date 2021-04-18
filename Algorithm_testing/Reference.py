import cv2
import numpy as np
from skimage.filters import threshold_multiotsu


def fun(p):
    if p == 1:
        return 85
    elif p == 2:
        return 170
    elif p == 3:
        return 255
    return 0


a = 1
b = 1

image_1 = cv2.imread('1.png')
image_2 = cv2.imread('2.png')

image_1 = cv2.GaussianBlur(image_1, (a, a), 0)
image_2 = cv2.GaussianBlur(image_2, (a, a), 0)

hsv_1 = cv2.cvtColor(image_1, cv2.COLOR_BGR2HSV)
hsv_2 = cv2.cvtColor(image_2, cv2.COLOR_BGR2HSV)

h1, s1, v1 = cv2.split(hsv_1)
blur_1 = cv2.GaussianBlur(v1, (b, b), 0)

h2, s2, v2 = cv2.split(hsv_2)
blur_2 = cv2.GaussianBlur(v2, (b, b), 0)

thresholds_1 = threshold_multiotsu(blur_1, classes=4)
thresholds_2 = threshold_multiotsu(blur_2, classes=4)

regions_1 = np.uint8(np.digitize(blur_1, bins=thresholds_1))
regions_2 = np.uint8(np.digitize(blur_2, bins=thresholds_2))

vfunc_1 = np.vectorize(fun)
regions_1 = np.uint8(vfunc_1(regions_1))
vfunc_2 = np.vectorize(fun)
regions_2 = np.uint8(vfunc_2(regions_2))

#ret_1, regions_1 = cv2.threshold(regions_1, 254, 255, cv2.THRESH_BINARY)
ret_2, regions_2 = cv2.threshold(regions_2, 254, 255, cv2.THRESH_BINARY)

grad_x_1 = cv2.Sobel(regions_1, cv2.CV_64F, 1, 0, ksize=3)
grad_y_1 = cv2.Sobel(regions_1, cv2.CV_64F, 0, 1, ksize=3)

abs_grad_x_1 = cv2.convertScaleAbs(grad_x_1)
abs_grad_y_1 = cv2.convertScaleAbs(grad_y_1)

edges_1 = cv2.addWeighted(abs_grad_x_1, 0.5, abs_grad_y_1, 0.5, 0)

grad_x_2 = cv2.Sobel(regions_2, cv2.CV_64F, 1, 0, ksize=3)
grad_y_2 = cv2.Sobel(regions_2, cv2.CV_64F, 0, 1, ksize=3)

abs_grad_x_2 = cv2.convertScaleAbs(grad_x_2)
abs_grad_y_2 = cv2.convertScaleAbs(grad_y_2)

edges_2 = cv2.addWeighted(abs_grad_x_2, 0.5, abs_grad_y_2, 0.5, 0)

while True:
    cv2.imshow('Frame_1', edges_1)
    cv2.imshow('Frame_2', edges_2)

    key = cv2.waitKey(30)
    if key == 27:
        break
cv2.destroyAllWindows()
