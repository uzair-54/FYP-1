import cv2
import numpy as np
import time
import helperFunctions as hf

thres = 0.60  # Threshold to detect object
nms_threshold = 0.2
cap = cv2.VideoCapture(0) #"C://Users//Muhammad Uzair//Desktop//la.mp4")
# cap.set(3,1280)
# cap.set(4,720)
# cap.set(10,150)

classNames = hf.getFileNames()

net = hf.nnSetup()
net.setInputSize(128, 128)
net.setInputScale(0.5 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

firebase, auth = hf.fireBaseConfigSetup()

opt = input("1) Create account \n2) Login \n")

email = input("Enter your email: ")
password = input("Enter your password: ")

if opt == "1":
    auth.create_user_with_email_and_password(email,password)
    print("account created use the services")

elif opt == "2":
    auth.sign_in_with_email_and_password(email, password)
    print("Logged in")

    pTime = time.time()

    while True:
            success, img = cap.read()
            classIds, confs, bbox = net.detect(img, confThreshold=thres)
            bbox = list(bbox)
            confs = list(np.array(confs).reshape(1, -1) [0])
            confs = list(map(float, confs))
            indices = cv2.dnn.NMSBoxes(bbox, confs, thres, nms_threshold)

            cTime = time.time()

            fps = 1 / (cTime - pTime)
            pTime = cTime
            print(fps,"FPS")
            # print(confs)
            for i in indices:

                box = bbox[i]
                x, y, w, h = box[0],box[1],box[2],box[3]
                hf.getFace(x,y,w,h,img)

                cv2.rectangle(img, (x, y), (x + w, h + y), (25, 25, 222),2)
                cv2.putText(img,classNames[classIds[i]-1].upper(),(box[0]+10,box[1]+30),cv2.FONT_HERSHEY_COMPLEX, 1, (255, 55, 255), 2)

            cv2.imshow("Output", img)
            cv2.waitKey(1)

