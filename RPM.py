import cv2
from cvzone.HandTrackingModule import HandDetector


cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
detector = HandDetector(detectionCon=0.8)
colorR = (255, 0, 255)

cx, cy, w, h = 100, 100, 200, 200



class DragRect():
    def __init__(self, posCenter, size = [200, 200]):
        self.posCenter = posCenter
        self.size = size

    def update(self, cursor):
        cx, cy = self.posCenter
        w, h = self.size

        # Condicional Rectangulo P
        if cx - w // 2 < cursor[0] < cx + w // 2 and \
                cy - h // 2 < cursor[1] < cy +h // 2:
            self.posCenter = cursor
            
rect = DragRect([150, 150])

while True:
    succes, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmList, _ = detector.findPosition(img)

    if lmList:

        l, _, _ = detector.findDistance(8, 12, img)
        print(l)
        if l < 30:
            cursor = lmList[8] #marca del cursor(fingers)
            #Update
            rect.update(cursor)

    ##Rectangulo(print)
    cx, cy = rect.posCenter
    w, h = rect.size
    cv2.rectangle(img, (cx-w//2, cy-h//2),
                    (cx+w//2, cy+h//2), colorR, cv2.FILLED)

    cv2.imshow("Image", img)
    cv2.waitKey(1)


