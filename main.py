import cv2
from setting_mode_window import *

cap = cv2.VideoCapture('video_.mp4')
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)


global img

while True:
    ok, img = cap.read()
    if not ok:
        break
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = (h_min, s_min, v_min)
    upper = (h_max, s_max, v_max)
    thresh = cv2.inRange(hsv, lower, upper)

    moments = cv2.moments(thresh, 1)
    dM01 = moments["m01"]
    dM10 = moments["m10"]
    dArea = moments["m00"]
    img2 = img
    if dArea > 40:
        x = int(dM10 / dArea)
        y = int(dM01 / dArea)
        img2 = cv2.circle(img.copy(), (x, y), 5, (0, 0, 255), -1)
        cv2.putText(img2, str(x) + '-' + str(y), (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    cv2.imshow("meow", img2)
    key_pressed = cv2.waitKey(1)
    if key_pressed == 27:
        print('pressed ESC')
        break
    elif key_pressed == 112:
        print('pressed P')
    elif key_pressed == 115:
        print('pressed S')  # setting mode
        h_min, s_min, v_min, h_max, s_max, v_max = entry_setting_mode(img)
        lower = (h_min, s_min, v_min)
        upper = (h_max, s_max, v_max)