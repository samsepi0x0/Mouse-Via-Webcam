import cv2
import mediapipe as mp
import time
import autopy
import numpy as np

widthC, heightC = 640, 480
widthS, heightS = autopy.screen.size()
frameRH, frameRW = 100, 75
smooth = 7

prevX, currX = 0, 0
prevY, currY = 0, 0

cap = cv2.VideoCapture(0)
cap.set(3, widthC)
cap.set(4, heightC)

previousTime = 0

mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img)

    points = dict()

    if results.multi_hand_landmarks:
        for id, lm in enumerate(results.multi_hand_landmarks[0].landmark):
            #print(id, lm)
            h, w, ch = img.shape # height width and channel
            cx, cy = int(lm.x * w), int(lm.y * h)
            # print(id, cx, cy)
            points[id] = (cx, cy)
            # find the index finger first
            # if id == 8:
            #    cv2.circle(img, (cx, cy), 15, (0,255,0), cv2.FILLED)
        #print(points)

        mpDraw.draw_landmarks(img, results.multi_hand_landmarks[0], mpHands.HAND_CONNECTIONS)

    if points:
        # tip of index is x1, y1 middle is x2,y2
        index = middle = False
        x1, y1 = points[8][0], points[8][1]
        x2, y2 = points[12][0], points[12][1]
        #print(x1, y1, x2, y2)

        cv2.rectangle(img, (frameRW, frameRH), (widthC - frameRW, heightC - frameRH), (255, 255, 255), 3)

        # is the index finger up?
        if y1 < points[6][1]:
            index = True
            #print("Index Finger is Raised.")

        if y2 < points[10][1]:
            middle = True
            #print("Middle Finger is Raised.")
           
        if index and not middle:
            x3 = np.interp(x1, (frameRW, widthC-frameRW), (0, widthS))
            y3 = np.interp(y1, (frameRH, heightC-frameRH), (0, heightS))
            cv2.circle(img, (x1, y1), 15, (0,255,0), cv2.FILLED)

            currX = prevX + (x3 - prevX) / smooth
            currY = prevY + (y3 - prevY) / smooth

            autopy.mouse.move(currX, currY)
            #print("Mouse moved")

            prevX, prevY = currX, currY
        if index and middle:
            cv2.circle(img, (x1, y1), 15, (0,255,0), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (0,255,0), cv2.FILLED)
            distance = int( ((y2 - y1)**2 + (x2-x1)**2) ** (1/2))
            # print(distance)
            if distance < 25:
                cv2.circle(img, (x1,y1), 15, (0,0,255), cv2.FILLED)    
                autopy.mouse.click()

    currentTime = time.time()
    FPS = 1 /  (currentTime - previousTime)
    previousTime = currentTime

    cv2.putText(img, str(int(FPS)), (15,45), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 3)

    cv2.imshow("Hand", img)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()