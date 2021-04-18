import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('Video', frame)
    key = cv2.waitKey(5)
    if key == 27:
        break
    elif key == ord('q'):
        cv2.imwrite('Pic.jpg', frame)
        print('success')

cap.release()
cv2.destroyAllWindows()
