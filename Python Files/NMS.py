import cv2
import numpy as np
import time
import helperFunctions as hf
import carControl as cc

thres = 0.60  # Threshold to detect object
nms_threshold = 0.2
cap = cv2.VideoCapture(0) #"C://Users//Muhammad Uzair//Desktop//la.mp4")
# cap.set(3,1280)
# cap.set(4,720)
# cap.set(10,150)

classNames = hf.getFileNames()

net = hf.nnSetup()
net.setInputSize(320, 320)
net.setInputScale(0.5 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)
pTime = time.time()

while True:
    success, img = cap.read()
    classIds, confs, bbox = net.detect(img, confThreshold=thres)
    bbox = list(bbox)
    confs = list(np.array(confs).reshape(1, -1)[0])
    confs = list(map(float, confs))
    indices = cv2.dnn.NMSBoxes(bbox, confs, thres, nms_threshold)

    cTime = time.time()

    fps = 1 / (cTime - pTime)
    pTime = cTime
    # print(fps,"FPS")
    # print(confs)
    for i in indices:

        box = bbox[i]
        x, y, w, h = box[0], box[1], box[2], box[3]

        faceWidthInFrame = hf.faceData(img)

        if faceWidthInFrame != 0:
            distance = hf.distanceFinder(hf.focallengthFound, hf.knownWidth, faceWidthInFrame)
            if (distance > 100):
                cc.forward()
                print("f")
            elif (distance < 50):
                cc.backward()
                print("b")

            cv2.putText(
                img, f"Distance: {round(distance, 2)} CM", (30, 35), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 55, 255), 2)

    cv2.imshow("Output", img)
    cv2.waitKey(1)
