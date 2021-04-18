import cv2
import numpy as np


def callback(*arg):
    pass


cv2.namedWindow('Video')
cv2.namedWindow('Settings')
cv2.namedWindow('Contour')

cap = cv2.VideoCapture(0)

cv2.createTrackbar('h1', 'Settings', 0, 255, callback)
cv2.createTrackbar('s1', 'Settings', 0, 255, callback)
cv2.createTrackbar('v1', 'Settings', 0, 255, callback)
cv2.createTrackbar('h2', 'Settings', 255, 255, callback)
cv2.createTrackbar('s2', 'Settings', 255, 255, callback)
cv2.createTrackbar('v2', 'Settings', 255, 255, callback)

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    h1 = cv2.getTrackbarPos('h1', 'Settings')
    s1 = cv2.getTrackbarPos('s1', 'Settings')
    v1 = cv2.getTrackbarPos('v1', 'Settings')
    h2 = cv2.getTrackbarPos('h2', 'Settings')
    s2 = cv2.getTrackbarPos('s2', 'Settings')
    v2 = cv2.getTrackbarPos('v2', 'Settings')

    h_min = np.array((h1, s1, v1), np.uint8)
    h_max = np.array((h2, s2, v2), np.uint8)

    thresh = cv2.inRange(hsv, h_min, h_max)

    cv2.imshow('Video', thresh)

    blur = cv2.medianBlur(thresh, 9)
    contours, hierarchy = cv2.findContours(blur, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    areas = []
    for i in range(len(contours)):
        areas.append(cv2.contourArea(contours[i]))

    N = areas.index(max(areas))

    x, y, w, h = cv2.boundingRect(contours[N])
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)

    moments = cv2.moments(thresh, 1)
    dM01 = moments['m01']
    dM10 = moments['m10']
    dArea = moments['m00']

    if dArea > 100:
        x = int(dM10 / dArea)
        y = int(dM01 / dArea)
        cv2.circle(frame, (x, y), 5, (0, 0, 255), -1)
        cv2.putText(frame, "%d-%d" % (x, y), (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow('Contour', frame)

    key = cv2.waitKey(5)
    if key == 27:
        break
    elif key == ord('q'):
        cv2.imwrite('Pic.jpg', frame)
        print('success')

cap.release()
cv2.destroyAllWindows()
print('h1 = %3i   s1 = %3i   v1 = %3i' % (h1, s1, v1))
print()
print('h2 = %3i   s2 = %3i   v2 = %3i' % (h2, s2, v2))
