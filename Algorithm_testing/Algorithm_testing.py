import cv2
import numpy as np
from skimage.filters import threshold_multiotsu
from time import time


def fun(p):
    if p == 1:
        return 85
    elif p == 2:
        return 170
    elif p == 3:
        return 255
    return 0


blur_kernel_size = 15

cv2.namedWindow('Video')

cap = cv2.VideoCapture('20201023_153816_3_ошибка_readme (1).avi')
#cap = cv2.VideoCapture('20210328_165529.avi')

fps = cap.get(cv2.CAP_PROP_FPS)
count_frame = 1
sec = 0
n_frame = sec * fps
while True:
    ret, frame = cap.read()
    # height = frame.shape[0]
    # width = frame.shape[1]
    print(count_frame)

    if count_frame < n_frame:
        pass
    else:
        start_time = time()

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        h, s, v = cv2.split(hsv)
        blur = cv2.GaussianBlur(v, (blur_kernel_size, blur_kernel_size), 0)

        # ret2, blur = cv2.threshold(blur, 150, 255, cv2.THRESH_TOZERO)

        thresholds = threshold_multiotsu(blur, classes=4)
        # th1, th2, th3 = thresholds
        print(thresholds)

        regions = np.uint8(np.digitize(blur, bins=thresholds))

        v_func = np.vectorize(fun)
        regions = np.uint8(v_func(regions))

        grad_x = cv2.Sobel(regions, cv2.CV_64F, 1, 0, ksize=3)
        grad_y = cv2.Sobel(regions, cv2.CV_64F, 0, 1, ksize=3)

        abs_grad_x = cv2.convertScaleAbs(grad_x)
        abs_grad_y = cv2.convertScaleAbs(grad_y)

        edges = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

        cv2.imshow('Video', regions)

        key = cv2.waitKey(int(1/fps*1000))
        if key == 27:
            break

        finish_time = time()
        work_time = finish_time - start_time
        print(work_time)
        print()
    count_frame += 1

cap.release()
cv2.destroyAllWindows()
