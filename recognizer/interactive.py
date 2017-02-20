import cv2
import numpy as np
from card_region_detector import *

SIZE = 750
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (SIZE, SIZE), None)
    cropped = crop_text_region(frame)
    if cropped:
        cv2.rectangle(frame, (cropped[0], cropped[1]), (cropped[2], cropped[3]), (0, 255, 0), 1)
        cv2.imshow('Text Crop', cropped)
    cv2.imshow('Orig', frame)

    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.destroyAllWindows()