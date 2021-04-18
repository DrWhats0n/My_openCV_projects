import cv2
import numpy as np


def filter(image, h1, s1, v1, h2, s2, v2):
    first_blur = cv2.medianBlur(image, 5)

    hsv_img = cv2.cvtColor(first_blur, cv2.COLOR_BGR2HSV)

    hsv_low = np.array([h1, s1, v1])
    hsv_high = np.array([h2, s2, v2])
    hsv_filter = cv2.inRange(hsv_img, hsv_low, hsv_high)
    return hsv_filter


def show(image, N, title, dx=0):
    x, y, w, h = cv2.boundingRect(contours[N])
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 255), 2)
    cv2.putText(image, title, (x+dx, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 1)
    cv2.namedWindow('Image', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


image = cv2.imread('Test.jpg')
search_query = input()

if search_query == 'car':
    hsv_filter = filter(image, 60, 3, 27, 116, 74, 181)

    second_blur = cv2.medianBlur(hsv_filter, 3)
    opening = cv2.morphologyEx(second_blur, cv2.MORPH_OPEN, (5, 5))
    dilation = cv2.dilate(opening, (9, 9), iterations=2)
    last_blur = cv2.medianBlur(dilation, 9)

    contours, hierarchy = cv2.findContours(last_blur, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    perimeters = []
    for i in range(len(contours)):
        perimeters.append(cv2.arcLength(contours[i], True))

    N = perimeters.index(max(perimeters))
    show(image, N, 'the beast machine')

elif search_query == 'man in red' or search_query == 'man in blue':
    if search_query == 'man in red':
        hsv_filter = filter(image, 175, 120, 106, 181, 217, 245)

        last_blur = cv2.medianBlur(hsv_filter, 5)

        contours, hierarchy = cv2.findContours(last_blur, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        N = 0
        show(image, N, 'the red dude', -45)

    else:
        hsv_filter = filter(image, 96, 72, 55, 116, 156, 212)

        last_blur = cv2.medianBlur(hsv_filter, 5)

        contours, hierarchy = cv2.findContours(last_blur, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        areas = []
        for i in range(len(contours)):
            areas.append(cv2.contourArea(contours[i]))

        N = areas.index(max(areas))
        show(image, N, 'the cut off blue dude')

elif search_query == 'dog' or search_query == 'horse':
    hsv_filter = filter(image, 2, 108, 0, 15, 188, 222)

    second_blur = cv2.medianBlur(hsv_filter, 7)
    dilation = cv2.dilate(second_blur, (9, 9), iterations=10)
    last_blur = cv2.medianBlur(dilation, 9)

    contours, hierarchy = cv2.findContours(last_blur, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    areas = []
    for i in range(len(contours)):
        areas.append(cv2.contourArea(contours[i]))

    horse_index = areas.index(max(areas))
    if search_query == 'dog':
        areas[horse_index] = 0
        dog_index = areas.index(max(areas))
        N = dog_index
        show(image, N, 'sobaken')
    else:
        N = horse_index
        show(image, N, 'horse')
else:
    print('error input')
