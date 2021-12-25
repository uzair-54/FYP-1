import cv2
import numpy as np
import time
import helperFunctions as hf
from face_lib import face_lib
FL = face_lib()

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

Known_distance = 76.2
Known_width = 14.3
def Focal_Length_Finder(measured_distance, real_width, width_in_rf_image):
    focal_length = (width_in_rf_image * measured_distance) / real_width
    return focal_length


def Distance_finder(Focal_Length, real_face_width, face_width_in_frame):
    distance = (real_face_width * Focal_Length) / face_width_in_frame

    return distance

face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def face_data(image):
    face_width = 0

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(gray_image, 1.3, 5)

    for (x, y, h, w) in faces:
        face_width = w

    return face_width

ref_image = cv2.imread("bb.jpg")

ref_image_face_width = face_data(ref_image)

Focal_length_found = Focal_Length_Finder(
    Known_distance, Known_width, ref_image_face_width)


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
                # hf.getFace(x,y,w,h,img)

                # cv2.rectangle(img, (x, y), (x + w, h + y), (25, 25, 222),2)
                # cv2.putText(img,classNames[classIds[i]-1].upper(),(box[0]+10,box[1]+30),cv2.FONT_HERSHEY_COMPLEX, 1, (255, 55, 255), 2)
                if FL.recognition_pipeline(ref_image,img)[0]:
                    cv2.rectangle(img, (x, y), (x + w, h + y), (0, 128, 0),2)
                    cv2.putText(img,classNames[classIds[i]-1].upper(),(box[0]+10,box[1]+30),cv2.FONT_HERSHEY_COMPLEX, 1, (255, 55, 255), 2)
                face_width_in_frame = face_data(img)

                if face_width_in_frame != 0:
                    Distance = Distance_finder(Focal_length_found, Known_width, face_width_in_frame)

                    cv2.putText(
                        img, f"Distance: {round(Distance, 2)} CM", (30, 35), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 55, 255), 2)

            cv2.imshow("Output", img)
            cv2.waitKey(1)

