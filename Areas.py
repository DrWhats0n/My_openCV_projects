import cv2

image_1 = cv2.imread('Frame_1.jpg')
image_2 = cv2.imread('Frame_2.jpg')
image_3 = cv2.imread('Frame_3.jpg')

image_2 = cv2.cvtColor(image_2, cv2.COLOR_BGR2GRAY)
ret_1, bw_2 = cv2.threshold(image_2, 90, 255, 0)

image_1 = cv2.cvtColor(image_1, cv2.COLOR_BGR2GRAY)
ret_2, bw_1 = cv2.threshold(image_1, 90, 255, 0)

image_3 = cv2.cvtColor(image_3, cv2.COLOR_BGR2GRAY)
ret_3, bw_3 = cv2.threshold(image_3, 90, 255, 0)

contours_1, hierarchy_1 = cv2.findContours(bw_1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
areas_1 = []
for i in range(len(contours_1)):
    areas_1.append(cv2.contourArea(contours_1[i]))
print('areas_1: ', areas_1)
print('length mas areas_1: ', len(contours_1))

contours_2, hierarchy_2 = cv2.findContours(bw_2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
areas_2 = []
for i in range(len(contours_2)):
    areas_2.append(cv2.contourArea(contours_2[i]))
print('areas_2: ', areas_2)
print('length mas areas_2: ', len(contours_2))

contours_3, hierarchy_3 = cv2.findContours(bw_3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
areas_3 = []
for i in range(len(contours_3)):
    areas_3.append(cv2.contourArea(contours_3[i]))
print('areas_3: ', areas_3)
print('length mas areas_3: ', len(contours_3))

cv2.drawContours(image_1, contours_1, -1, (125, 125, 125), 3)
cv2.drawContours(image_2, contours_2, -1, (125, 125, 125), 3)
cv2.drawContours(image_3, contours_3, -1, (125, 125, 125), 3)

while True:
    cv2.imshow('Frame_1', image_1)
    cv2.imshow('Frame_2', image_2)
    cv2.imshow('Frame_3', image_3)

    key = cv2.waitKey(30)
    if key == 27:
        break
cv2.destroyAllWindows()
