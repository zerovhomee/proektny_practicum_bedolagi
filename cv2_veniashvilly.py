import cv2
import numpy as np

def main():
    video_path = "video_2024-05-24_13-49-59.mp4"
    check_github = 1000000

    cap = cv2.VideoCapture(video_path)
    cv2.namedWindow('frame')
    kernel = np.ones((5,5), np.uint8)

    def nothing(x):
        pass
    cv2.createTrackbar('HL', 'frame', 0, 255, nothing)
    cv2.createTrackbar('SL', 'frame', 0, 255, nothing)
    cv2.createTrackbar('VL', 'frame', 0, 255, nothing)

    cv2.createTrackbar('H', 'frame', 0, 180, nothing)
    cv2.createTrackbar('S', 'frame', 0, 255, nothing)
    cv2.createTrackbar('V', 'frame', 0, 255, nothing)


    fps = cap.get(cv2.CAP_PROP_FPS)
    wait_time = int(1000 / fps)

    while True:
        ret, frame = cap.read()
        frame = cv2.bilateralFilter(frame, 9, 75, 75)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        hl = cv2.getTrackbarPos('HL', 'frame')
        sl = cv2.getTrackbarPos('SL', 'frame')
        vl = cv2.getTrackbarPos('VL', 'frame')
        h = cv2.getTrackbarPos('H', 'frame')
        s = cv2.getTrackbarPos('S', 'frame')
        v = cv2.getTrackbarPos('V', 'frame')

        lower = np.array([hl, sl, vl])
        upper = np.array([h, s, v])
        mask = cv2.inRange(hsv, lower, upper)
        res = cv2.bitwise_or(frame,frame,mask=mask)
        opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        clos = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

        cont, h = cv2.findContours(clos,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        cont = sorted(cont, key = cv2.contourArea, reverse=True)

        for x in range(len(cont)):
            area = cv2.contourArea(cont[x])
            if area > 300:
                x,y,w,h = cv2.boundingRect(cont[x])
                frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255),2)

        cv2.drawContours(frame, cont, -1, (255, 0, 0), 4)


        cv2.imshow('mask', mask)
        cv2.imshow('fr', frame)
        if cv2.waitKey(wait_time) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
