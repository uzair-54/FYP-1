import cv2
# from random import randrange
import time

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

 
print("No Error")

pTime = time.time()

while True:
        success, img = cap.read()

        cTime = time.time()

        
        grayscaled_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
        
        for x, y, w, h in face_coordinates:
            cv2.rectangle(img, (x, y), (x + w, y + h), (25, 25, 222),5)

        fps = 1 / (cTime - pTime)
        pTime = cTime
        print(fps,"FPS")
        
        cv2.imshow("Output", img)
        cv2.waitKey(1)