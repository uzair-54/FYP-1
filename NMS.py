import cv2
import numpy as np
import time
from config import firebaseConfig
import pyrebase
from face_lib import face_lib

FL = face_lib()
thres = 0.60  # Threshold to detect object
nms_threshold = 0.2
cap = cv2.VideoCapture(0) #"C://Users//Muhammad Uzair//Desktop//la.mp4")
cap.set(3,1280)
cap.set(4,720)
cap.set(10,150)

classNames = []
classFile = 'additional Files//coco.names'
with open(classFile,'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')


configPath = 'additional Files//ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'additional Files//frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

config = firebaseConfig
firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

opt = input("1) Create account \n2) Login \n")

email = input("Enter your email: ")
password = input("Enter your password: ")

if opt == "1":
    auth.create_user_with_email_and_password(email,password)
    print("account created use the services")

else:
    auth.sign_in_with_email_and_password(email, password)
    print("Logged in")

pTime = time.time()

while True:
        success, img = cap.read()
        no_of_faces, faces_coors = FL.faces_locations(img)
        classIds, confs, bbox = net.detect(img, confThreshold=thres)
        bbox = list(bbox)
        confs = list(np.array(confs).reshape(1, -1) [0])
        confs = list(map(float, confs))
        indices = cv2.dnn.NMSBoxes(bbox, confs, thres, nms_threshold)

        no_of_faces, faces_coors = FL.faces_locations(img)
        print(faces_coors)
        cTime = time.time()

        fps = 1 / (cTime - pTime)
        pTime = cTime
        print(fps,"FPS")
        # print(confs)
        for i in indices:

            box = bbox[i]
            x, y, w, h = box[0],box[1],box[2],box[3]
            cv2.rectangle(img, (x, y), (x + w, h + y), (255, 0, 222),2)
            cv2.putText(img,classNames[classIds[i]-1].upper(),(box[0]+10,box[1]+30),cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("Output", img)
        cv2.waitKey(1)