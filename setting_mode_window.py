import cv2

h_min = 0
s_min = 0
v_min = 0
h_max = 200
s_max = 255
v_max = 255


def entry_setting_mode(img):
    window_name = 'settings'
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, 1000, 350)
    cv2.createTrackbar('H min', window_name, 0, 200, lambda x: None)
    cv2.createTrackbar('S min', window_name, 0, 255, lambda x: None)
    cv2.createTrackbar('V min', window_name, 0, 255, lambda x: None)
    cv2.createTrackbar('H max', window_name, 0, 200, lambda x: None)
    cv2.createTrackbar('S max', window_name, 0, 255, lambda x: None)
    cv2.createTrackbar('V max', window_name, 0, 255, lambda x: None)
    cv2.setTrackbarPos('H max', window_name, 200)
    cv2.setTrackbarPos('S max', window_name, 255)
    cv2.setTrackbarPos('V max', window_name, 255)

    def save_params():
        h_min = cv2.getTrackbarPos('H min', window_name)
        s_min = cv2.getTrackbarPos('S min', window_name)
        v_min = cv2.getTrackbarPos('V min', window_name)
        h_max = cv2.getTrackbarPos('H max', window_name)
        s_max = cv2.getTrackbarPos('S max', window_name)
        v_max = cv2.getTrackbarPos('V max', window_name)

    cv2.createButton('save', save_params, cv2.QT_PUSH_BUTTON | cv2.QT_NEW_BUTTONBAR)
    while True:
        h_min = cv2.getTrackbarPos('H min', window_name)
        s_min = cv2.getTrackbarPos('S min', window_name)
        v_min = cv2.getTrackbarPos('V min', window_name)
        h_max = cv2.getTrackbarPos('H max', window_name)
        s_max = cv2.getTrackbarPos('S max', window_name)
        v_max = cv2.getTrackbarPos('V max', window_name)
        lower = (h_min, s_min, v_min)
        upper = (h_max, s_max, v_max)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        thresh = cv2.inRange(hsv, lower, upper)
        img2 = cv2.bitwise_and(img, img, mask=thresh)
        key_pressed = cv2.waitKey(10)
        cv2.imshow('setting2', img2)

        if key_pressed == 27:
            print('pressed ESC')
            cv2.destroyWindow('settings')
            cv2.destroyWindow('setting2')
            break
