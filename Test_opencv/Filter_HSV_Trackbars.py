import cv2
import numpy as np


def callback(*arg):
    pass


cv2.namedWindow('Picture', cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('Settings', cv2.WINDOW_NORMAL)

img = cv2.imread('Test.jpg')
img = cv2.medianBlur(img, 5)
cv2.imshow('Picture', img)
cv2.waitKey(0)

cv2.createTrackbar('h1', 'Settings', 0, 255, callback)
cv2.createTrackbar('s1', 'Settings', 0, 255, callback)
cv2.createTrackbar('v1', 'Settings', 0, 255, callback)
cv2.createTrackbar('h2', 'Settings', 255, 255, callback)
cv2.createTrackbar('s2', 'Settings', 255, 255, callback)
cv2.createTrackbar('v2', 'Settings', 255, 255, callback)

while True:
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h1 = cv2.getTrackbarPos('h1', 'Settings')
    s1 = cv2.getTrackbarPos('s1', 'Settings')
    v1 = cv2.getTrackbarPos('v1', 'Settings')
    h2 = cv2.getTrackbarPos('h2', 'Settings')
    s2 = cv2.getTrackbarPos('s2', 'Settings')
    v2 = cv2.getTrackbarPos('v2', 'Settings')

    h_min = np.array((h1, s1, v1), np.uint8)
    h_max = np.array((h2, s2, v2), np.uint8)

    thresh = cv2.inRange(hsv, h_min, h_max)

    cv2.imshow('Picture', thresh)

    key = cv2.waitKey(5)
    if key == 27:
        break

cv2.destroyAllWindows()
print(h_min)
print()
print(h_max)
