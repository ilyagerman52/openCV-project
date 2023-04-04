import cv2
from setting_mode_window import *

cap = cv2.VideoCapture(0)

global img

while True:
    ok, img = cap.read()
    if not ok:
        break
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = (h_min, s_min, v_min)
    upper = (h_max, s_max, v_max)
    thresh = cv2.inRange(hsv, lower, upper)
    img = cv2.bitwise_and(img, img, mask=thresh)

    cv2.imshow("meow", img)
    key_pressed = cv2.waitKey(1)
    if key_pressed == 27:
        print('pressed ESC')
        break
    elif key_pressed == 112:
        print('pressed P')
    elif key_pressed == 115:
        print('pressed S')  # setting mode
        entry_setting_mode(img)
